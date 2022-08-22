#!/usr/bin/env python
# coding: utf-8

# In[5]:


num = int(input("Enter a number: "))
if num > 0:
    print("+1")
elif num == 0:
    print("0")
elif num < 0:
    print("-1")
    


# In[19]:


x = int(input("Enter your initial number"))
y = int(input("Enter the final number"))
for i in range(x ,y+1,1):
    if(i%10 == 7):
        continue
    if('0' in str(i)):
        continue
    print(i)
    


# In[24]:


n = int(input("Enter a range: "))
s = 0
for i in range(1,n+1,1):
    s += i**3
print(s)


# In[1]:


c = int(input("Enter a temperature(in celcius): "))
f = c/5*9 + 32
print(f)
far = int(input("Enter a temperature(in farenheit): "))
cel = (far-32)*5/9
print(cel)


# In[28]:


size = int(input("what is the size of the grid: "))

for row in range(size,1-1,-1):
    for columns in range(size,1-1,-1):
        print(f'({row},{columns})',end ='')
    print()


# In[1]:


num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
guess = int(input("Enter the product of the 2 numbers entered(you get 3 tries)"))
num = 0
while(num_1*num_2 != guess):
    print("You are incorrect! Try again:")
    guess = int(input("Enter the product of the 2 numbers entered(you get 3 tries)"))
    num += 1
    if(num == 2)and(num_1*num_2 != guess):
        print("You lose!")
        break
    if(num_1*num_2 == guess):
        print("You win!")

