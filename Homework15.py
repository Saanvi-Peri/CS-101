#!/usr/bin/env python
# coding: utf-8

# In[4]:


inpt = int(input("Enter a number"))
def multiply3(inpt):
    if inpt % 3 == 0:
        print(inpt*5)
multiply3(inpt)


# In[28]:


x = int(input("Enter a number"))
def multiply3(x):
    def is_divisible_by_3(x):
        return bool(x % 3 == 0)
    is_divisible_by_3(x)
    if is_divisible_by_3(x) == True:
        print(x*5)
    else:
        print(x)
multiply3(x)


# In[17]:


inpt = int(input("Enter a number"))
def multiply3(inpt):
    b = lambda a: a % 3
    if b(inpt) == 0:
        print(inpt*5)
    else:
        return(inpt)
multiply3(inpt)


# In[27]:


npt = input("Enter a word: ")
def word(npt):
    x = lambda a: a in npt
    if (x("y")):
        return bool(x("y"))
word(npt)


# In[41]:


lst = ["Jake" "wonders" "why" "you" "are" "looking" "at" "the" "sky"] 
def word(lst):
    result = map(lambda a: a in lst, lst)
    if (result("y")):
        return bool(result("y"))
word(lst)


# In[43]:


lst = ["Jake" "wonders" "why" "you" "are" "looking" "at" "the" "sky"] 
result = map(lambda a: a in lst, numbers) 
print(list(result("y"))) 

