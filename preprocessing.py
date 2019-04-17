import pandas  as pd
import seaborn as sns
import matplotlib.pyplot as plt    # Data Visualization


# the effect of various factors on students reading, writing and maths score
data=pd.read_csv('F:\Anjus_projects\studentAnalysis\StudentsPerformance.csv')
#print(data.head())
sns.heatmap(data.corr(), annot = True, cmap='inferno') #showing the correlation between the features
plt.show()# this output will show the high correlation between  a student's reading score & writing score, reading score & math score and writing score & math score

#Plotting the distribution of students marks
#math score distribution
plt.figure(figsize=(8,5))
sns.distplot(data['math score'], kde = False, color='g', bins = 20)
plt.ylabel('Frequency')
plt.title('Math Score Distribution')
plt.show() #Most students have their math score in the range of 60 to 80


#Reading Score
plt.figure(figsize=(8,5))
sns.distplot(data['reading score'], kde = False, color='r', bins = 30)
plt.ylabel('Frequency')
plt.title('Reading Score Distribution')
plt.show() #Most students have their reading score in the range of 60 to 80


#Writing Score
plt.figure(figsize=(8,5))
sns.distplot(data['writing score'], kde = False, color='blue', bins = 30)
plt.ylabel('Frequency')
plt.title('Writing Score Distribution')
plt.show()#Most students have their writing score in the range of 60 to 80

#Bar Plot of Scores according to gender
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
sns.barplot(x = 'gender', y = 'reading score', data = data)

plt.subplot(1,3,2)
sns.barplot(x = 'gender', y = 'writing score', data = data)

plt.subplot(1,3,3)
sns.barplot(x = 'gender', y = 'math score', data = data)
plt.show() #Males have higher math score than Females, whereas Females have higher scores in reading and writing than Males

plt.tight_layout()
# Bar plot of Scores on the basis of Race/Ethnicity
plt.figure(figsize=(14,4))

plt.subplot(1,3,1)
sns.barplot(x = 'race/ethnicity', y = 'reading score', data = data)
plt.xticks(rotation = 90)

plt.subplot(1,3,2)
sns.barplot(x = 'race/ethnicity', y = 'writing score', data = data)
plt.xticks(rotation = 90)

plt.subplot(1,3,3)
sns.barplot(x = 'race/ethnicity', y = 'math score', data = data)
plt.xticks(rotation = 90)
plt.show()
plt.tight_layout()


#Bar plots of Scores on the basis of Test Prepration Course
plt.figure(figsize=(14,4))
plt.subplot(1,3,1)
sns.barplot(x = 'test preparation course', y = 'reading score', hue = 'gender', data = data)
#plt.show()

plt.subplot(1,3,2)
sns.barplot(x = 'test preparation course', y = 'writing score',hue = 'gender', data = data)
#plt.show()

plt.subplot(1,3,3)
sns.barplot(x = 'test preparation course', y = 'math score',hue = 'gender', data = data)
plt.show()# Students who have completed the Test Prepration Course have scores higher in all three categories than those who haven't taken the course

plt.tight_layout()
#plt.show()


# Bar Plots of Scores on the basis of Parent's Education Level
plt.figure(figsize=(13,5))

plt.subplot(1,3,1)
sns.barplot(x = 'parental level of education', y = 'reading score', data = data)
plt.xticks(rotation = 90)

plt.subplot(1,3,2)
sns.barplot(x = 'parental level of education', y = 'writing score', data = data)
plt.xticks(rotation = 90)

plt.subplot(1,3,3)
sns.barplot(x = 'parental level of education', y = 'math score', data = data)
plt.xticks(rotation = 90)
plt.show() #Student's whose parents have a Master's degree have scored higher compared to others whereas Student's whose parent's went to high school have obtained low marks compared to others
plt.tight_layout()

#Bar Plots of Scores on the basis of Types of Luch

plt.figure(figsize=(14,4))

plt.subplot(1,3,1)
sns.barplot(x = 'lunch', y = 'reading score', data = data)

plt.subplot(1,3,2)
sns.barplot(x = 'lunch', y = 'writing score', data = data)

plt.subplot(1,3,3)
sns.barplot(x = 'lunch', y = 'math score', data = data)
plt.show()#Students who availed standard luch have scored higher in all the three categories compared to students who have taken free/ reduced lunch.

plt.tight_layout()


