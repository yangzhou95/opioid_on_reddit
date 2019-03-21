setwd("~/TTU-SOURCES/harvey-classifier/r")

data = read.table("data/Clustering5.txt", sep = '\t', header = TRUE, colClasses=c(NA,NA,"NULL"))

str(data)

# plot data point to see its distribution
plot(data$Column1, data$Column2, main="Data Scatterplot", col=rgb(0,100,0,50,maxColorValue=255), pch=16)

# 1. apply k-mean and visualize clusters
km.out = kmeans(x=data, centers=3 , nstart=20)
# plot clusters: pch=20 => symbol is circle; cex = scale ratio
plot(data , col=(km.out$cluster +1), main =" K - Means Clustering Results with K=3" , xlab ="" , ylab ="" , pch=20 , cex=2)


## 2. hierarchical clustering
dev.off()
hc.complete = hclust( dist( data ), method="complete")
hc.average  = hclust( dist( data ), method="average")
hc.single   = hclust( dist( data ), method="single")

par(mfrow = c(1 ,3) )
plot(hc.complete , main ="Complete Linkage ", xlab = "", sub ="", cex =.9)
plot(hc.average , main ="Average Linkage ", xlab = "", sub ="" , cex =.9)
plot (hc.single , main ="Single Linkage ", xlab = "", sub ="", cex =.9)
par(mfrow=c(1,1))

## 3. spectral clustering
dev.off()
library(kernlab)
myData = as.matrix(data)
sc = specc(myData, centers=3)
plot(myData, main = "Spectral Clustering with Centers=3",  col=sc + 1, xlab = "", ylab ="", pch=20, cex=2)      


## 4. db scan
dev.off()
library(dbscan)
db = dbscan(myData, eps = 2, minPts = 5)
plot(myData , col = db$cluster + 1, main ="DBScan with eps=2" , xlab ="" , ylab ="" , pch=20 , cex=2)


