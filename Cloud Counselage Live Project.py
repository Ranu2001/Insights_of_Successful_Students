#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Current working directory:
import os 
os.getcwd()


# In[2]:


os.chdir("C:\\Users\\ranub\\Downloads")


# In[3]:


import pandas as pd 
import numpy as np


# In[4]:


data = pd.read_excel("data_analystdata.xlsx")


# In[5]:


data


# In[6]:


data.head()


# In[7]:


data.tail()


# # BASIC QUESTIONS

# # How many unique students are included in the dataset

# In[8]:


# Assuming the dataset has a column named 'Email ID' for student identification
unique_students = data['Email ID'].nunique()

print(f"Number of unique students: {unique_students}")


# # What is the average GPA of the students

# In[9]:


# Assuming the dataset has a column named 'CGPA' for GPA
average_gpa = data['CGPA'].mean()

print(f"Average GPA of the students: {average_gpa:.2f}")


# # What is the distribution of student's across different graduation years

# In[13]:


import matplotlib.pyplot as plt
# Assuming the dataset has a column named 'Year of Graduation' for graduation years
graduation_counts = data['Year of Graduation'].value_counts().sort_index()

# Plotting the distribution
plt.figure(figsize=(10, 6))
graduation_counts.plot(kind='bar', color='purple')
plt.title('Distribution of Students Across Graduation Years')
plt.xlabel('Graduation Year')
plt.ylabel('Number of Students')
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()


# # What is the distribution of student's experience with python programming

# In[14]:


# Assuming the dataset has a column named 'Experience with python (Months)' for experience levels
experience_counts = data['Experience with python (Months)'].value_counts().sort_index()

# Plotting the distribution
plt.figure(figsize=(8, 6))
experience_counts.plot(kind='bar', color='violet')
plt.title("Distribution of Students' Experience with Python Programming")
plt.xlabel('Python Experience Level')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# # How does the GPA vary among different colleges (Show top 5 results only)

# In[16]:


# Assuming the dataset has columns 'College Name' and 'CGPA'
college_gpa = data.groupby('College Name')['CGPA'].mean().sort_values(ascending=False)

# Show top 5 colleges with highest average GPA
top_colleges = college_gpa.head(5)

# Plotting the top 5 colleges and their average GPA
plt.figure(figsize=(10, 6))
top_colleges.plot(kind='bar', color='lightgreen')
plt.title('Top 5 Colleges by Average GPA')
plt.xlabel('College')
plt.ylabel('Average GPA')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# # Are there any outliers in the quantity (Number of courses completed) attribute

# In[17]:


import seaborn as sns


# In[18]:


# Assuming the dataset has a column named 'Quantity' for number of courses completed
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['Quantity'])
plt.title('Boxplot of Quantity (Number of Courses Completed)')
plt.xlabel('Quantity')
plt.show()


# # What is the average GPA for student from each city

# In[19]:


# Assuming the dataset has columns 'City' and 'CGPA'
average_gpa_by_city = data.groupby('City')['CGPA'].mean()

# Print the average GPA for each city
for city, avg_gpa in average_gpa_by_city.items():
    print(f"Average GPA for students from {city}: {avg_gpa:.2f}")


# # Can we identify any relationship between family income and GPA

# In[20]:


# Assuming the dataset has columns 'Family Income' and 'CGPA'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Family Income', y='CGPA', data=data)
plt.title('Scatter Plot of Family Income vs. GPA')
plt.xlabel('Family Income')
plt.ylabel('GPA')
plt.tight_layout()
plt.show()


# # MODERATE QUESTIONS

# # Which event tend to attract more students from specific fields of study

# In[21]:


# Assuming the dataset has columns 'Events' and 'Attendee Status' for event name and student field
plt.figure(figsize=(12, 6))
sns.countplot(x='Events', hue='Attendee Status', data=data)
plt.title('Event Attendance by Student Fields')
plt.xlabel('Event Name')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Student Field')
plt.show()


# # Do students in leadership positions during their college years tend to have higher GPAs or better expected salary

# In[22]:


# Assuming the dataset has columns 'Leadership- skills', 'CGPA', and 'Expected salary (Lac)'
plt.figure(figsize=(12, 6))
sns.boxplot(x='Leadership- skills', y='CGPA', data=data)
plt.title('GPA vs. Leadership Position')
plt.xlabel('Leadership Position')
plt.ylabel('GPA')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Leadership- skills', y='Expected salary (Lac)', data=data)
plt.title('Expected Salary vs. Leadership Position')
plt.xlabel('Leadership Position')
plt.ylabel('Expected Salary')
plt.tight_layout()
plt.show()


# # How many students are graduating by the end of 2024

# In[23]:


# Assuming the dataset has a column named 'Year of Graduation' for graduation years
graduating_by_2024 = data[data['Year of Graduation'] <= 2024]
num_graduating = len(graduating_by_2024)

print(f"Number of students graduating by the end of 2024: {num_graduating}")


# # How many students know about the event from their colleges (Which of these Top 5 colleges)

# In[24]:


# Assuming 'College' is the column containing college names and 'Knows About Event' is the column indicating if they know about the event
# You might need to adjust column names based on your data
top_5_colleges = data['College Name'].value_counts().head(5)

print("Top 5 Colleges and the Number of Students Who Know About the Event:")
print(top_5_colleges)


# # How does the expected salary vary based on factors like 'GPA', 'Famliy income', 'Experience with Python(Months)'

# In[26]:


print(data.dtypes)


# In[28]:


print(data['Family Income'].dtype)


# In[29]:


data['Family Income'] = pd.to_numeric(data['Family Income'], errors='coerce')


# In[30]:


# Assuming 'data' is your DataFrame
data['Family Income'] = pd.to_numeric(data['Family Income'], errors='coerce')

# Now, try your mathematical operation again
result = data['Family Income'] * 2  

# Check the result or perform your intended operation
print(result)


# In[31]:


import seaborn as sns
import matplotlib.pyplot as plt

# # Create a pairplot to visualize relationships among variables
sns.pairplot(data, x_vars=['CGPA', 'Experience with python (Months)', 'Family Income'], y_vars=['Expected salary (Lac)'], kind='reg')
plt.show()


# # Find the total number of students who attended the events related to data science (From all data science related courses)

# In[84]:



data = {
    'Email ID': ['george@xyz.com', 'cynthia@xyz.com', 'theodore@xyz.com', 'martha@xyz.com', 'chauncey@xyz.com'],
    'Events': ['Data Visualization using Power BI', 'Artificial Intelligence', 'Hello ML and DL', 'Product Marketing', 'IAC - Q&A'],
    'Attendee Status': [True, False, True, True, True]
}

# Create a DataFrame
data = pd.DataFrame(data)

# Filter for Data Science-related courses and event attendance
data_science_courses = ['Data Visualization using Power BI', 'Artificial Intelligence']
filtered_data = data[(data['Events'].isin(data_science_courses)) & (data['Attendee Status'] == True)]

# Calculate the total number of students who attended data science events
total_attendees = filtered_data['Email ID'].nunique()

print(f'Total number of students who attended data science events: {total_attendees}')


# # Those who have CGPA and More experience in language those who had high expectations for salary (Avg)

# In[72]:


# Assuming 'CGPA', 'Experience with python (Months)', and 'Expected salary (Lac)' are the relevant columns
filtered_data = data[(data['CGPA'] >= 9.0) & (data['Experience with python (Months)'] > 6)]

high_salary_expectations = filtered_data[filtered_data['Expected salary (Lac)'] > filtered_data['Expected salary (Lac)'].mean()]

print(f"The number of students with high CGPA and more experience in language, and high salary expectations is: {len(high_salary_expectations)}")


# # Which promotion channel is brings in more student participations for the event

# In[73]:


# Assuming 'How did you come to know about this event?' and 'Attendee Status' are the relevant columns
channel_attendance = data.groupby('How did you come to know about this event?')['Quantity'].sum()

# Find the promotion channel with the highest attendance
most_successful_channel = channel_attendance.idxmax()
max_attendance = channel_attendance.max()

print(f"The most successful promotion channel is '{most_successful_channel}' with a total attendance of {max_attendance} students.")

# Plotting the attendance by promotion channel
plt.figure(figsize=(30,12))
channel_attendance.sort_values(ascending=False).plot(kind='bar')
plt.xlabel('How did you come to know about this event?')
plt.ylabel('Total Attendance')
plt.title('Attendance by Promotion Channel')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# # Ploting the most succesful promotions channel is whatsapp with a total attedance of 1067 students for better understanding

# In[75]:


# Data
channel = 'Whatsapp'
total_attendance = 1067

# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(channel, total_attendance, color='skyblue')
plt.xlabel('Promotion Channel')
plt.ylabel('Total Attendance')
plt.title('Most Successful Promotion Channel')
plt.text(channel, total_attendance + 20, str(total_attendance), ha='center', va='bottom', fontsize=12, color='black')
plt.tight_layout()

plt.show()

