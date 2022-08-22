#!/usr/bin/env python
# coding: utf-8

# In[4]:


def the_sum(*args):
    total = 0
    for i in args:
        total += i
    print(total/len(args))
    return total
print(the_sum(1, 2, 3, 6, 5, 7, 8, 9, 4))


# In[10]:


#Create a function that returns a/b. If b is zero, the function returns "NAN"
#string. If a or b are not valid numbers (integer or float) the function also
#returns "NAN".
def division(a, b):
    try:
        total = a/b
    except TypeError:
        total = ["You provided the wrong answer"]
    return total
print(division(20, 4))


# In[13]:


def name_age(**kwargs):
    for name, age in kwargs.items():
        print("%s is %s years old" %(name,age))
name_age(Saanvi = 13, Savir = 11, Vidya = 41, Ram = 43)


# In[32]:


user_input = str(input("Enter your name: "))
def initials(user_input):
    split = user_input.split()
    print(split)
    for i in split:
            print(i[0], end="")
initials(user_input)


# In[40]:


user_input = str(input("Enter your name: "))
def initials(user_input):
    split = user_input.split()
    print(split)
    return [i[0] for i in split]
print(initials(user_input))


# In[44]:


D = {}
user_input = str(input("Enter your name: "))
def add_name(D):
    for initials, f_l_name in D.items():
        print("%s, %s" %(initials, f_l_name))
    def initials(user_input):
        split = user_input.split()
        print(split)
        return [i[0] for i in split]
s = initials(user_input)
add_name(D)

