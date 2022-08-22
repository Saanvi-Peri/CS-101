#!/usr/bin/env python
# coding: utf-8

# In[14]:


capitals = {
            "USA": "Washington DC", 
            "India": "New Dehli", 
            "Italy": "Rome", 
            "Belarus": "Minsk", 
            "Bosnia and Herzegovina": "Sarajevo"
           }
y = input("Write the name of a country and I will tell you the capital: ")
x = capitals.get(y)
print(f"The capital of {y} is {x}")


# In[16]:


capitals = {
            "USA": "Washington DC", 
            "India": "New Dehli", 
            "Italy": "Rome", 
            "Belarus": "Minsk", 
            "Bosnia and Herzegovina": "Sarajevo"
           }
count = 0
while(count < 6):
    y = input("Write the name of a country and I will tell you the capital: ")
    x = capitals.get(y)
    print(f"The capital of {y} is {x}")
    count = count + 1


# In[6]:


currency = {
            "British pound": "0.731464",
            "Indian Rupee": "73.244134",
            "Australian Dollar": "1.285809",
            "Canadian Dollar": "1.270703",
            "Singapore Dollar": "1.322972",
            "Swiss Franc": "0.886058",
            "Malaysian Ringgit": "4.055472"
            }

currency_name = input("Write the name of the currency you use. I will convert it to US dollars: ")
currency_value = int(input("Write how much of the curency you have: "))
#print(currency_value)
converted_currency_value = currency.get(currency_name)
ccv_float = float(converted_currency_value)
#print(type(ccv_float)
value = currency_value/ccv_float
print(f"You have {value} US dollars.")


# In[15]:


movies = {
        "Inception": "2020", 
        "Airplane": "1980", 
        "My cousin Vinny": "1992", 
        "Murder on the Orient Express": "1974", 
        "Jumanji": "2019"
        }

values = movies.values()
print(values)
greater_values = {}
for i in values:
    a = float(i)
    if(a > 2017):
        greater_values["1"] = i
print(greater_values)


# In[48]:


movies = {
        "Inception": "2020", 
        "Airplane": "1980", 
        "My cousin Vinny": "1992", 
        "Murder on the Orient Express": "1974", 
        "Jumanji": "2019"
        }

movies_copy = movies.copy()
for x in movies_copy:
    print(x)

for x in movies_copy:
    print(movies_copy[x])
for i in movies_copy[x]:
    i = int(i)
    if i < 2017:
        del i
print(movies_copy)


# In[ ]:





# In[ ]:


string = str(values)
greater_values = []
for i in values:
    i = int(i)
    if i > 2017:
        greater_values.append(i)
        for i in greater_values:
            if i in movies:
                greater_values.append(movies[i])
print(f"The movies released after 2017 are {greater_values}.")         

