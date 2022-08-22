#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1
name = str(input("Enter a name: "))
while True:
    try: 
        height_ft = float(input("Enter their height in feet: "))
        break
    except ValueError:
        print("Enter a number please! Try again.")
print(f"{name}s height in centimeters is {height_ft*30.48} cm")


# In[32]:


#Problem 2
while True:
    try:
        num = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Please enter a number. Try again: ")

index = 0
num_1 = str(num)
#print("You gave:", num_1)

while True:
    try:
        x = num_1[index]
        if("3" == x):
            print("There is a 3 in the number. Program terminates.")
            break
        index += 1
    except IndexError:
        print("There are no 3s in this number. Program terminates.")
        break


# In[31]:


#Problem 3
while True:
    num_1 = int(input("Please input a number here: "))
    num_2 = int(input("Please input another number here: "))
    try:
        q = num_1 / num_2
        print(f"The quotient of these two numbers is {q}.")
        break
    except ZeroDivisionError:
        print("Please pick another number.")


# In[10]:


#Problem 4
counter = 1
x = 1
while(counter < 366):
    counter += 1
    x = (x + 1/50*x)
print(x)


# In[13]:


#Problem 4
x = 1
for counter in range(1,365,1):
    x = x*(1 + 1.0/50)
print(x)


# In[16]:


#Problem 4
x = (1 + 1.0/50)**364
print(x)


# In[36]:


#Problem 5
x = 1
for counter in range(1,365,1):
    x = x*(1 + 1.0/50)
    if((counter % 14) == 0):
        x = (x - 0.1*x)
print(x)


# In[35]:


#Problem 5
counter = 1
x = 1
while(counter < 366):
    counter += 1
    x = (x + 3/10*x)
    if((counter % 14) == 0):
        x = (x - 0.1*x)
print(x)

