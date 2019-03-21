setwd("~/TTU-SOURCES/harvey-classifier/r")

tweets = read.csv("data/labeled-rescue.csv", stringsAsFactors = FALSE)
str(tweets)

nrow(tweets)

firstThousandRows = tweets[1:1000,]

firstThousandRows$text = gsub("\"", '', firstThousandRows$text)

write.csv(firstThousandRows, file = "data/labeled-rescue-1000.csv", row.names=FALSE)