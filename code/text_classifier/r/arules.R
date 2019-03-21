library(arules)
library(arulesViz)

setwd("~/TTU-SOURCES/harvey-classifier/r")

tr <- read.transactions("data/transactions.csv", format = "basket", sep=",", skip = 1)

frequentItems <- eclat (tr, parameter = list(supp = 0.05, maxlen = 50)) # calculates support for frequent items
inspect(frequentItems)

itemFrequencyPlot(tr, topN=15, type="absolute", main="Item Frequency") # plot frequent items


rules <- apriori (tr, parameter = list(supp = 0.02, conf = 0.5)) # Min Support as 0.001, confidence as 0.8.
rules_conf <- sort (rules, by="confidence", decreasing=TRUE) # 'high-confidence' rules.
inspect(head(rules_conf)) # show the support, lift and confidence for all rules

plot(rules)