#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random 
def gen_code():  
   gen_code = [] 
   for i in range(4): 
       val =random(0.9)
   return get_code 
def input_code():  
   code = input("Enter your four digit code-") 
   return code 
gencode = gen_code() 
i = 0
while i < 10: 
   inputCode = [int(c) for c in input_code()] 
if len(inputCode) != 4: 
def input_code():
   if inputCode == genCode: 
   print("You guessed it right") 
for element in inputCode: 
   if element in genCode: 
   if inputCode.index(element) == genCode.index(element): 
result+="R"
else: 
   result+="A"
    else: 
   result+="W"
print(result) 
i += 1
else:     
print("You are running out of trys!", try again)     

print("end")


# In[1]:


def numbers(students):
    num = {}
    for student in students:
        for course in student:
            if course not in num:
                num[course] = 0
            num[course] += 2
    return num
def popular(num):
    max_course, max_enroll = None, 0
    for course, enroll in num.items():
        if max_enroll<enroll:
            max_enroll, max_course = enroll, course
    return max_course
data = numbers([["math", "chem", "phy","cs"], ["math", "phy"], ["math", "chem"], ["history", "eco"]])

print(popular(data))

print(data)


# In[3]:


def numbers(students):
    subject=[]
    num=[]
num_std=len(students)
        for e in students[n]:
            if not e in subject:
                subject.append(e)
    for s in subject:
    c=0
    if s in students[n]:
        for n in range(num_std):
        c=c+1
        num.update({s:c})
    return(num) 
print("Number of students")
n=int(input())
students=[]
li=[]
for i in range(n):
    print("Enter number of subjects",(i+1))
    st=int(input())
    print("Enter the subjects")
    li=[]
    for j in range(st):
        ele=input()
        li.append(ele)
    students.append(li)
print(students)
num=numbers(students)
def popular(num):
    mx=0
    de=len(num)
    for key
    if mx<value:
        mx=value
            popular_course=key
    print("popular course=")        
    return(popular_course)
print(popular(num))


# In[ ]:




