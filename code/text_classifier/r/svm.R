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
library(e1071)
library(caTools)
library(RTextTools)
library(ROCR)

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

  # cleanTweets = as.data.frame(as.matrix(sparseTweets))
  # colnames(cleanTweets) = make.names(colnames(cleanTweets))
  # cleanTweets$label = tweets$label
  #
  # str(cleanTweets)
  #
  # return(cleanTweets)

  return (sparseTweets)
}

tweets = cleanTweet(tweets)


# create split with 70% is TRUE (this will be used as training set)
spl = sample.split(tweets$label, SplitRatio = 0.5)
trainSamples = subset(tweets, spl == TRUE)
testSamples = subset(tweets, spl == FALSE)

train = as.data.frame(trainSamples$tweet, stringsAsFactors = FALSE)
colnames(train) = c("tweet")

test = as.data.frame(testSamples$tweet, stringsAsFactors = FALSE)
colnames(test) = c("tweet")

combinedSVMTweets = rbind(train, test)

trainLabel = as.data.frame(trainSamples$label, stringsAsFactors = FALSE)
colnames(trainLabel) = c("label")

testLabel = as.data.frame(testSamples$label, stringsAsFactors = FALSE)
colnames(testLabel) = c("label")

combinedSVMLabel = rbind(trainLabel, testLabel)

cleanTweetsDTMMatrix = createDTMCleanTweet(combinedSVMTweets)
str(cleanTweets)
# set.seed(456)


## trainSparse now has 700 rows (70%) 


trainSize = nrow(train)


container <- create_container(cleanTweetsDTMMatrix, combinedSVMLabel$label, trainSize=1:trainSize, testSize=(trainSize+1):nrow(combinedSVMLabel), virgin=FALSE)

SVM <- train_model(container,"SVM")                 
SVM_CLASSIFY <- classify_model(container, SVM)
analytics <- create_analytics(container, cbind(SVM_CLASSIFY))
summary(analytics)

length(analytics@document_summary$MANUAL_CODE)
length(analytics@document_summary$SVM_LABEL)



svmResult = data.frame(svm.probs = analytics@document_summary$SVM_PROB, svm.actuals = analytics@document_summary$MANUAL_CODE)
write.csv(svmResult, file = "data/svm-predict.csv", row.names=FALSE)


## accuracy test
confusionMatrix = table(predict = analytics@document_summary$SVM_LABEL, actual = analytics@document_summary$MANUAL_CODE)
confusionMatrix

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

svmmodel.prediction<-prediction(analytics@document_summary$SVM_PROB, analytics@document_summary$MANUAL_CODE)
svmmodel.performance<-performance(svmmodel.prediction,"tpr","fpr")


graphics.off()
plot(svmmodel.performance, avg= "threshold", col="red", lwd=2, main="ROC curve!")

