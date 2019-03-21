library(wordcloud2)
library(SnowballC)
library(stringr)
library(ggplot2)
library(tidytext)
library(tidyr)
library(dplyr)

setwd("~/TTU-SOURCES/harvey-classifier/r")

tweets = read.csv("data/labeled-rescue-1000.csv", stringsAsFactors = FALSE)

cleanTweet = function(tweets) {
  replace_reg = "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"
  unnest_reg = "([^A-Za-z_\\d#@']|'(?![A-Za-z_\\d#@]))"
  
  tweets = tweets %>% 
    mutate(text = str_replace_all(text, replace_reg, ""),
           id = row_number()
           )
  
  tweets$tweet = tweets$text
  tweets$text = NULL
  
  return(tweets)
}

tweets = cleanTweet(tweets)

str(tweets)

additionalStopWords = c("harvey")
additionalStopWords_df <- data_frame(lexicon="custom", word = additionalStopWords)


custom_stop_words = stop_words
custom_stop_words <- bind_rows(custom_stop_words, additionalStopWords_df)


words = tweets %>%
  unnest_tokens(word, tweet) %>%
  anti_join(custom_stop_words, by = c("word" = "word"))
  

write.csv(words, file = "data/items.csv", row.names=FALSE)
