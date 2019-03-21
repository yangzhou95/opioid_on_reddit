# Set seed for reproducible results
set.seed(100)

# Packages
library(tm) # Text mining: Corpus and Document Term Matrix
library(class) # KNN model
library(SnowballC) # Stemming words
library(ROCR)
library(stringr)
library(caTools)


setwd("~/TTU-SOURCE/harvey-classifier/r")

# Read csv with two columns: text and category
df <- read.csv("data/labeled-rescue-1000.csv", sep =",", header = TRUE)
df$text = str_replace_all(df$text,"[^[:graph:]]", " ") 

# Create corpus
docs <- Corpus(VectorSource(df$text))

# Clean corpus
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, stemDocument, language = "english")

# Create dtm
dtm <- DocumentTermMatrix(docs)

# Transform dtm to matrix to data frame - df is easier to work with
mat.df <- as.data.frame(data.matrix(dtm), stringsAsfactors = FALSE)

nrow(mat.df)
ncol(mat.df)

# Column bind category (known classification)
mat.df <- cbind(mat.df, df$label)

# Change name of new column to "category"
colnames(mat.df)[ncol(mat.df)] <- "labeled-rescue"
ncol(mat.df)

# Split data by rownumber into two equal portions
set.seed(456)

# create split with 70% is TRUE (this will be used as training set)
spl = sample.split(mat.df$`labeled-rescue`, SplitRatio = 0.5)
trainSamples = subset(mat.df, spl == TRUE)
testSamples = subset(mat.df, spl == FALSE)
clTrain = as.factor(trainSamples$`labeled-rescue`)
clTest = testSamples$`labeled-rescue`
nrow(train)
# train <- sample(nrow(mat.df), ceiling(nrow(mat.df) * .50))
# test <- (1:nrow(mat.df))[- train]

train = trainSamples[, ,!colnames(trainSamples) %in% "labeled-rescue"]
test = testSamples[, ,!colnames(testSamples) %in% "labeled-rescue"]


doKNN = function(train, test, clTrain, clTest, kValue) {
  knn.pred <- knn(train, test, clTrain, prob = TRUE, k = kValue)
  
  # Confusion matrix
  conf.mat <- table("Predictions" = knn.pred, Actual = clTest)
  conf.mat
  
  # Accuracy
  a = conf.mat[2,2]
  a
  b = conf.mat[1,2]
  b
  c = conf.mat[2,1]
  c
  d = conf.mat[1,1]
  d
  
  precision = p = a / (a+c)
  p
  recall = r = a / (a+b)
  r
  f.measure = f = 2*a / (2*a + b + c)
  f
  
  accuracy <- sum(diag(conf.mat))/nrow(test) * 100
  accuracy
  
  message(paste("TP = a = ", a, ", FN = b =", b, ", FP = c =", c, ", TN = d =", d))
  message(paste("k =", kValue, "accuracy=", accuracy, " p =", p, "r =", r, "f-measure =", f))
  
  # Create data frame with test data and predicted category
  # df.pred <- cbind(knn.pred, modeldata[test, ])
  # write.table(df.pred, file="output.csv", sep=";")
  
  
  
  prob <- attr(knn.pred , "prob")
  #knn.pred <- prediction(prob, clTest)
  
  
  
  return (prob)
}

colors <- c('red', 'blue', 'green', 'yellow', 'black') # 5 colors
min = 1
max = 1

graphics.off()

for(i in  min:max) {
  prob = doKNN(train, test, clTrain, clTest, kValue = i)
  knn.pred <- prediction(prob, clTest)
  knn.perf <- performance(knn.pred, "tpr", "fpr")
  
  knnResult = data.frame(knn.probs = prob, knn.actuals = clTest)
  write.csv(knnResult, file = "data/knn-predict.csv", row.names=FALSE)
  
  
  if (i > min) {
    plot(knn.perf, add = TRUE, avg= "threshold", col=colors[i], lwd=2)
  }
  else {
    plot(knn.perf, avg= "threshold", col=colors[i], lwd=2, main="ROC curve!")
    
  }
}

