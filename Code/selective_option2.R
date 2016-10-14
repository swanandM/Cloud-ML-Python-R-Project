#2)
#GRE __ Decision __ Season  __ degree ___ only new gre

setwd("/Users/Abhinav/Documents/Programming in Cloud/MidTermProject")
mydata <- read.csv("finaldataset.csv",header = TRUE)
x <- commandArgs()
GRE <- as.integer(x[6])
#GRE
Desision_input <-x[7]
#Desision_input
seaason_input <- x[8]
#seaason_input
degree_input <- x[9]
#degree_input
sum12 = (mydata$sumGRE > GRE & mydata$Decision==Desision_input & mydata$Season== seaason_input & mydata$Degree==degree_input & mydata$Is_new_GRE=="TRUE")
mydata[sum12, c("Univ_Name","Major","sumGRE")] 