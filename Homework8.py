#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create my list
my_list = [1,6.0,False,'dog']
#append method
my_list.append(True)
#append method adds a specified element to the end of the list
print(my_list)
#[1,6.0,False,'dog',True]

#extend method
my_list.extend([3,'kitty',9.0])
#extend method adds all elements of a list to another list
print(my_list)
#[1,6.0,False,'dog',True,3,'kitty',9.0]

#insert method
my_list.insert(2,'north pole')
#insert an item at the defined index
print(my_list)
#[1,6.0,'north pole',False,'dog',True,3,'kitty',9.0]

#remove method
my_list.remove('dog')
#removes an item from the list
print(my_list)
#[1,6.0,'north pole',False,True,3,'kitty',9.0]

#pop method
a = my_list.pop(3)
#removes and returns an element at the given index
print(my_list)
print(a)
#[1,6.0,'north pole',True,3,'kitty',9.0]
#False

#clear method
my_list.clear()
#removes all items from a list
print(my_list)
#[]

my_list = [1,3,'north pole',True,3,'kitty',9.0]
#index method
index = my_list.index('kitty')
#returns the index of the first matched item
print(index)
#5

my_list = [1,3,'north pole',True,3,'kitty',9.0]

#count method
a = my_list.count(3)
#returns the count of the number of items passed as an argument(the number of times a certain element is counted)
print(a)
#2

my_list = ['e', 'a', 'u', 'o', 'i']
#sort method
my_list.sort()
#Sort items in a list in ascending order
print(my_list)
#['a', 'e', 'i', 'o', 'u']

my_list = [1,3,'north pole',True,3,'kitty',9.0]
#reverse method
my_list.reverse()
#reverses the order of items in list
print(my_list)
#[9.0, 'kitty', 3, True, 'north pole', 3, 1]

my_list = [1,3,'north pole',True,3,'kitty',9.0]
#copy method
new_list = my_list.copy()
new_list.append(5)
print(my_list)
print(new_list)
#[1,3,'north pole',True,3,'kitty',9.0]
#[1,3,'north pole',True,3,'kitty',9.0,5]


# In[2]:


my_family = ['Vidya', 'Ram', 'Saanvi', 'Savir', 'Syamala', 'Sastry', 'Janaki', 'Prabhakar']
my_family_ages = [41,42,12,11,67,72,67,74]
for i in range(len(my_family)):
    print(f'{my_family[i]} is {my_family_ages[i]} years old.')


# In[1]:


my_list = []
i  = 0
while(input("Do you want to enter a students name?")!= "no"):
    name = input("Enter the students name.")
    my_list.append(name)
for i in range(len(my_list)):
    a = input(f"Is {my_list[i]} absent?")
    if(a == "yes"):
        new_list = my_list.pop(i)
        print(my_list)
print(f'{new_list[i]} was in class today.')
break


# In[ ]:




