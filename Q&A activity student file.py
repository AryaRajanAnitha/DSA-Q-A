#!/usr/bin/env python
# coding: utf-8

# ## 1. Complete the following code to find the area of an equilateral triangle. Output should be as displayed

# In[3]:


import math
side = float(input("Enter the side of the equilateral triangle: "))
area = ((math.sqrt(3))/4)*pow(side,2)
print("Area of the equilateral triangle",area)


# ## 2. Write a program to count the number of each characters in a string

# In[13]:


a=input("Enter the string ")
out = {x : a.count(x) for x in set(a)} 
print ("number of all characters in the String:\n "+ str(out))


# ## 3. Write a program to find the area and perimeter of a rectangle using functions

# In[16]:


length=float(input("Enter the length of rectangle: "))
width=float(input("enter the width of rectangle: "))
def rectangle(length,width):
    area =length * width
    perimeter =2 * (length+width)
    print("area of rectangle = ",area) 
    print("perimeter of rectangle = ",perimeter)
    
rectangle(length,width) 


# ## 4. Write a program to print the fibonacci series till a specified number

# In[32]:


num = int(input("Enter the Range Number: "))
First_val = 0
Second_val = 1
for n in range(0, num):
            if(n <= 1):
                        temp = n
            else:
                        temp = First_val + Second_val
                        First_val = Second_val
                        Second_val = temp
            print(temp)


# ## 5. Complete the following code to find the minimum of 3 number using conditional statements. Output should be as displayed

# In[35]:


a,b,c = input("Enter three numbers followed by  : ").split()

print("First number :",a)
print("Second number :",b)
print("Third number :",c)
if(a==b==c): 
    print("Entered numbers are equal!!!")
elif(a<b and a<c):
    print(a," is smallest")
elif(b<a and b<c):
    print(b," is smallest")
else:
    print(c," is smallest")


# ## 6. Write a program to print star pyramind. The number of rows should be taken as input from the user

# In[45]:


num=int(input("Enter the number of rows"))
for i in range(0, num):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")


# ## 7. Complete the following code to convert hour into seconds. Output should be as displayed

# In[37]:


def to_seconds(t):
    t=t*60*60
    return t
time_in_hours = int(input("Enter time in Hours"))
print(time_in_hours ," Hour is equal to" ,to_seconds(time_in_hours) ," Seconds")
#to_seconds(t)


# ## 8. Write a program to print multiplication table as below

# In[38]:


n=int(input('Enter a number to find the multiplication table :'))
for i in range(1,11):
    print(i,' x ',n,' = ',n*i)


# ## 9. Write a program to take your 5 favorite food as list and print each as 'I like Biriyani'

# In[43]:


fav_food=input("Enter your five favorite food").split()
for i  in range(0,5):
    print("I like ",fav_food[i])


# In[ ]:




