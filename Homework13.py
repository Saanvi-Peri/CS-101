#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def product():
    a = int(input("enter a number"))
    b = int(input("enter another number"))
    print(a*b)

product()


# In[ ]:


def product():
    a = int(input("enter a number"))
    b = int(input("enter another number"))
    return(a*b)

product()


# In[ ]:


def fruit_colors():
    a = ["apple", "apricot", "pineapple", "custard apple", "dragon fruit"]
    b = ["red", "orange", "yellow", "green", "purple"]
    x = zip(a,b)
    print(dict(x))
fruit_colors()


# In[22]:


def division():
    while True:
            try:
                a = int(input("Please enter a number: "))
                b = int(input("enter another number"))
                break
            except ValueError:
                     print("NAN")
            except ZeroDivisionError:
                print(NAN)
division()


# In[4]:


def number():
    while True:
            try:
                a = int(input("Please enter a number: "))
                if(a == "quit"):
                    print("NAN")
                break
            except ValueError:
                print("Oops!  That was an invalid number. Try again: ")
number()


# In[30]:


def list_of_values():
    list = []
    while True:
        a = input("Please enter a value: ")
        list.append(a)
        b = input("Do you want to enter another value?")
        if b == "yes":
            print("okay")
            continue
        else:
            print("okay")
            print(list)
            break 
list_of_values()


# In[37]:


def values():
    l = []
    while True:
        a = input("Please enter a value: ")
        l.append(a)
        b = input("Do you want to enter another value?")
        if b == "yes":
            print("okay")
            continue
        else:
            print("okay")
            #print(l)
            break 
    print(set(l))
values()

