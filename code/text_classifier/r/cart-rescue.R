# This file will classify tweets into two categories (negative-flu-shot and none-negative-flu-shot)
# once classifiation is done, two separated files are created serve as input for association rules

library(devtools)
library(tm)
library(tidytext)
library(tidyr)
library(dplyr)
library(SnowballC)
library(topicmodels)
library(ggplot2)
library(stringr)

set.seed(123)
setwd("~/TTU-SOURCES/harvey-classifier/r")

# without pre-processing data
#tweets = read.csv("labeled-tweet-flu-shot.csv", stringsAsFactors = FALSE)

# with pre-processing data
tweets = read.csv("data/labeled-rescue-1000.csv", stringsAsFactors = FALSE)

str(tweets)
sum(tweets$label)

cleanTweet = function(tweets) {
  replace_reg = "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"
  unnest_reg = "([^A-Za-z_\\d#@']|'(?![A-Za-z_\\d#@]))"
  
  tweets = tweets %>% 
    mutate(text = str_replace_all(text, replace_reg, ""))
  
  tweets$tweet = tweets$text
  tweets$text = NULL
  
  return(tweets)
}

createDTMCleanTweet = function(tweets) {
  
  # Create Corpus
  tweetCorpus = Corpus(VectorSource(tweets$tweet))
  
  # convert documents into lowercase
  tweetCorpus = tm_map(tweetCorpus, content_transformer(tolower))
  tweetCorpus = tm_map(tweetCorpus, content_transformer(removePunctuation))
  
  str(tweetCorpus)
  
  #tweetCorpus = tm_map(tweetCorpus, content_transformer(removeWords), c("flu", "shot", "shots", "feel", "like", "thank", "can", "may", "get", "got", "gotten", "think", "flushot", stopwords("english")))
  tweetCorpus = tm_map(tweetCorpus, content_transformer(removeWords), c(stopwords("english")))
  
  tweetCorpus = tm_map(tweetCorpus, stemDocument)
  
  dtmTweets = DocumentTermMatrix(tweetCorpus)
  dtmTweets
  
  # find frequency
  findFreqTerms(dtmTweets, lowfreq = 20)
  
  
  # Filter out sparse terms by keeping only terms that appear in 0.3% or more of the revisions
  sparseTweets = removeSparseTerms(dtmTweets, 0.997)
  sparseTweets
  
  cleanTweets = as.data.frame(as.matrix(sparseTweets))
  colnames(cleanTweets) = make.names(colnames(cleanTweets))
  cleanTweets$label = tweets$label
  
  str(cleanTweets)  
  
  return(cleanTweets)
}

tweets = cleanTweet(tweets)

cleanTweets = createDTMCleanTweet(tweets)

library(caTools)
# set.seed(456)

# create split with 70% is TRUE (this will be used as training set)
spl = sample.split(cleanTweets$label, SplitRatio = 0.7)
trainSparse = subset(cleanTweets, spl == TRUE)
testSparse = subset(cleanTweets, spl == FALSE)
## trainSparse now has 700 rows (70%) 
nrow(trainSparse)
str(testSparse)
## testSparse now has 300 rows (30%)
nrow(testSparse)
# CART Model
library(rpart)
library(rpart.plot)
tweetCART <- rpart(label ~., data=trainSparse, method="class")
prp(tweetCART)


# Predict using the trainig set. Because the CART tree assigns the same predicted probability to each leaf node and there are a small number of leaf nodes compared to data points, we expect exactly the same maximum predicted probability.
predictCart <- predict(tweetCART, newdata=testSparse, type="class")
summary(predictCart)

str(predictCart)
str(testSparse$label)

## accuracy test
confusionMatrix = table(testSparse$label, predictCart)
confusionMatrix
confusionMatrix[1,1]

a = confusionMatrix[2,2] 
b = confusionMatrix[2,1]
c = confusionMatrix[1, 2]
d = confusionMatrix[1, 1]
precision = a / (a + c)
precision

recall = a / (a + b)
recall

fMeasure = 2*a / (2*a + b + c)
fMeasure

accuracy = (a + d) / (a + b + c +d)
accuracy

message(paste("accuracy: ", accuracy, "; precision: ", precision, "; recall: ", recall, "; f-measure: ", fMeasure))
