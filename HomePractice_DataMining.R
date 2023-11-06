#Q1 logistic regression 
library(readxl)
dataset1 <- read_excel("/Users/lijiaqi/Downloads/Ch9_Q18_Data_File.xlsx")
View(dataset)
model1<-glm(y~x1+x2, family=binomial, data=dataset)
summary(model1)
predict(model1,data.frame(x1=12,x2=8),type='response')

#Q2 KNN
library(caret)
library(ggplot2)
library(lattice)
myData1<-scale(df2[,2:3])		
myData1<-data.frame(myData1, df2$y)
View(myData1)
colnames(myData1)[3]<-'y'
myData1$y<-as.factor(myData1$y)
View(myData1)

set.seed(1)						# data partition for cross-validation
myIndex<-createDataPartition(myData1$y,p=0.6,list=FALSE)
trainSet<-myData1[myIndex,]
validationSet<-myData1[-myIndex,]
myCtrl<-trainControl(method='cv',number=10)			# set for 10-fold cross validation
myGrid<-expand.grid(.k=c(1:10)) 				# set range of k for KNN optimization

# create KNN algorithm and select optimal K
set.seed(1)							# create KNN algorithm
KNN_fit<-train(y~.,data=trainSet,method='knn',trControl=myCtrl,tuneGrid=myGrid)
KNN_fit	

KNN_Class <- predict(KNN_fit, newdata = validationSet)
confusionMatrix(KNN_Class, validationSet$y, positive = '1')

KNN_Class_prob <- predict(KNN_fit, newdata = validationSet, type='prob')
KNN_Class1 <- as.factor(ifelse(KNN_Class_prob[,2]>0.25, '1', '0'))
confusionMatrix(KNN_Class1, validationSet$y, positive = '1')

# check accuracies
library(gains)
library(pROC)
validationSet$Enroll <- as.numeric(as.character(validationSet$Enroll)) 
gains_table <- gains(validationSet$Enroll, KNN_Class_prob[,2])
gains_table
plot(c(0, gains_table$cume.pct.of.total*sum(validationSet$Enroll))~c(0, gains_table$cume.obs), xlab = "# of cases", ylab = "Cumulative", main="Cumulative Lift Chart", type="l")
lines(c(0, sum(validationSet$Enroll))~c(0, dim(validationSet)[1]), col="red", lty=2)
barplot(gains_table$mean.resp/mean(validationSet$Enroll), names.arg=gains_table$depth, xlab="Percentile", ylab="Lift", ylim=c(0,3), main="Decile-Wise Lift Chart")
roc_object <- roc(validationSet$Enroll, KNN_Class_prob[,2])
plot.roc(roc_object)
auc(roc_object)

# score the score file
trainscale<- preProcess(myData[,2:4], method=c('center', 'scale'))  
myScoreData1<-predict(trainscale, myScoreData)	              # scale the ScoreData with myData parameters
KNN_Score<-predict(KNN_fit,newdata=myScoreData1)	              
myScoreData<-data.frame(myScoreData,KNN_Score)
View(myScoreData)	

#Q3 Decision Tree
library(readxl)
myData3 <- read_excel("/Users/lijiaqi/Downloads/Ch13_Q33_Data_File.xlsx")
View(myData3)
library(caret)
library(rpart)
library(rpart.plot)
library(forecast)

suppressWarnings(RNGversion("3.5.3"))
set.seed(1)
myIndex <- createDataPartition(myData3$y, p=0.7, list=FALSE)
trainSet <- myData3[myIndex,]
validationSet <- myData3[-myIndex,]

# building a defualt tree
set.seed(1)
default_tree <- rpart(y ~., data = trainSet, method = "anova")
prp(default_tree, type = 1, extra = 1, under = TRUE)

# building the full tree and obtain cp table
set.seed(1)
full_tree <- rpart(y ~ ., data = trainSet, method = "anova", cp = 0, minsplit = 2, minbucket = 1)
printcp(full_tree)

# obtain the best pruned tree 
bp_tree <- prune(full_tree, cp = 2.5092e-02)
prp(bp_tree, type = 1, extra = 1, under = TRUE)
# obtain the minimum error tree 
me_tree <- prune(full_tree, cp = 2.4083e-02)
prp(me_tree, type = 1, extra = 1, under = TRUE)

# check for best pruned tree's validation error
predicted_value <- predict(bp_tree, validationSet)
accuracy(predicted_value, validationSet$y)
# apply the best pruned tree to score new customers
predicted_value_score <- predict(bp_tree, myScoreData)
predicted_value_score

#Q4 Association
library(arules)
myData<-read.transactions("/Users/lijiaqi/Downloads/Ch14_Q48_Data_File_CSV.csv", format='basket',sep=',')
inspect(myData[1:5])  

#item frequencies 
itemFrequency(myData)  
itemFrequencyPlot(myData) 

#generate, sort, and view rules
rules<-apriori(myData,parameter = list(minlen=2,supp=0.1,conf=0.5))
srules<-sort(rules,by='lift',decreasing='TRUE')
inspect(srules)

#Q5 Cluster
library(cluster)
library(readxl)
myData5 <- read_excel("/Users/lijiaqi/Downloads/Ch14_Q25_Data_File.xlsx")
View(myData5)

#standardize data
myData5 <- scale(myData5[,1:7])
myData5_subset<-myData5[,1:3]

suppressWarnings(RNGversion("3.5.3"))
set.seed(1)
kResult <- pam(myData5_subset, k=3)
summary(kResult)

#generate plots
plot(kResult)



