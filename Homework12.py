#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = ("My name is Saanvi.")
tuple(string)
print(string)
#the tuple() method converts the string to a tuple and when you print it,there are no quotes


# In[5]:


tuple = (1, 3, 5, 7, 9)
product = 1
for i in tuple:
    product *= i
print(product)


# In[29]:


numbers = ((1, 3), (4, 5), (9, 2), (7, 6))
sum = 0
average = []
for i in numbers:
    for x in i:
        average.append(x)
for i in average:
    sum += i 
length = len(average)
print(sum/length)


# In[ ]:


numbers = ((1, 3), (4, 5), (9, 2), (7, 6))
s = 0
l = 0
for i in numbers:
    for x in i:
        s += x
        l += 1
print(s, l)
print(s/l)

print(2)
s = sum(
    map(sum, numbers)
)
l = sum(map(len, numbers))
print(s, l, s/l)


# In[30]:


number_tuple = ("1","3","4","5","9","2","7","6")
l = []
for i in number_tuple:
    l.append(int(i))
print(l)


# In[12]:


a =((5, 8, 6, 1), (3, 0, 2, 7), (6, 4, 9, 3), (2, 9, 5, 6))
sum(a[0])
counter = 0
new_list = []
while(counter < 4):
    for i in a[counter]:
        new_list.append(i)
    counter += 1
    break
print(new_list)


# In[6]:


a =((5, 8, 6, 1), (3, 0, 2, 7), (6, 4, 9, 3), (2, 9, 5, 6))
counter = 0
res=[]
for counter in range(len(a[0])):
    res.append(sum([x[counter] for x in a]))

print(str(res))


# In[8]:


a =((5, 8, 6, 1), (3, 0, 2, 7), (6, 4, 9, 3), (2, 9, 5, 6))
res = [ sum([x[counter] for x in a]) for counter in range(len(a[0])) ]
print(str(res))


# In[30]:




