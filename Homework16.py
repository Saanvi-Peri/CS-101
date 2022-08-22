#!/usr/bin/env python
# coding: utf-8

# In[4]:


mystr = "I love bread!"
myster = mystr.split()
lst = []
for i in myster:
    lst.append(len(i))
print(lst)


# In[12]:


mystr = "I love bread!"
list(map(len, mystr.split()))


# In[11]:


mystr = "I love bread!"
[len(i) for i in mystr.split()]


# In[29]:


last = [7, 97, 27, 37, 57, 47, 67, 70, 71, 76, 73, 74, 75, 72, 77, 78, 79, 87, 17]
last.sort()
print(last)


# In[38]:


# a function that returns True or False
last = [7, 97, 27, 37, 57, 47, 67, 70, 71, 76, 73, 74, 75, 72, 77, 78, 79, 87, 17]
def random_list(x):
    last.sort
    return(last)
lost = [27, 37, 57, 47, 67, 70, 71, 76, 73, 74]

W = list(lost)

W2 = list(filter(random_list, W))
print(W2)

