#1)
#Uni Name ___ GRE __ Decision __ Season  __ degree__ only new gre 
setwd("/Users/Abhinav/Documents/Programming in Cloud/MidTermProject")
mydata <- read.csv("finaldataset.csv",header = TRUE)
x <- commandArgs()
Univ_Name <- x[6]
Univ_Name
GRE <- as.integer(x[7])
GRE
Decision_input <- x[8]
Decision_input
seaason_input <- x[9]
seaason_input
degree_input <- x[10]
degree_input

sum11 = mydata$School_Name== Univ_Name  & mydata$sumGRE > as.integer(GRE) & mydata$Decision==Decision_input & mydata$Season==seaason_input & mydata$Degree==degree_input & mydata$Is_new_GRE=="TRUE"
mydata[sum11, c("Major","sumGRE")] 


print("General information of the University")
gre=summary(mydata$School_Name== Univ_Name & mydata$sumGRE < 300 & mydata$Decision=="Accepted")
gre1=as.integer(gre[[3]])
print("Number of students having GRE score less than 300 and received admission at this university")
gre1

#Students Applied/Accepted/Acceptance Rate at this Uni
acc1=summary(mydata$School_Name ==Univ_Name)
y=as.integer(acc1[[3]])
print("Number of students applied to this university")
y

z=summary(mydata$School_Name==Univ_Name & mydata$Decision=="Accepted")
x=as.integer(z[[3]])
print("Number of Students got accepted in this University")
x
r = (x/y)*100
print("Acceptance Rate of the University is")
r

#Season & university
sum1 = sum(mydata$School_Name== Univ_Name &  mydata$Season==seaason_input)
print("Students applied to this university in this Season")
sum1

ms=summary(mydata$School_Name==Univ_Name & mydata$Degree=="MS")
ms1=as.integer(ms[[3]])
print("Number of Students applied for MS at this University")
ms1

phd=summary(mydata$School_Name==Univ_Name & mydata$Degree=="PhD")
phd1=as.integer(phd[[3]])
print("Number of Students applied for PhD at this University")
phd1

status=summary(mydata$School_Name==Univ_Name & mydata$Status=="American")
status1=as.integer(status[[3]])
print("Number of American students at this university")
status1

g= mydata$School_Name == Univ_Name & mydata$Decision == "Accepted"
g1=mydata[g,]
g2=g1$sumGRE
print("Minimum GRE score accepted in this school")
min(g2)

g3 = ifelse(g2<340,g2,0)
print("Student with maximum GRE score in this school")
max(g3)