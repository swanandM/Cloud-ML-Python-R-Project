#3)Uni_Name __ Decision __ Season __ Only new gre

setwd("/Users/Abhinav/Documents/Programming in Cloud/MidTermProject")
mydata <- read.csv("finaldataset.csv",header = TRUE)
x <- commandArgs()

Univ_Name <- x[6]
#Univ_Name
Desision_input <-x[7]
#Desision_input
seaason_input <- x[8]
#seaason_input

sum13 = (mydata$School_Name== Univ_Name & mydata$Decision== Desision_input & mydata$Season== seaason_input & mydata$Is_new_GRE=="TRUE")
mydata[sum13, c("Univ_Name","Major","sumGRE","Degree")] 