#!/usr/bin/env python
# coding: utf-8

# In[65]:


movies = ["Inception", "Clue", "Airplane"]

ratings = [100,99,97]

movies.append("Back to the future")

ratings.append(98)

for i in range(len(movies and ratings)):
    
    print(f"{movies[i]}. Rating: {ratings[i]}")
    
print(sum(ratings)/len(ratings))

print(min(movies and ratings))

a = (min(ratings))

c = ratings.index(a)
#print(c)

movies.remove(movies[c])

ratings.remove(a)

print(movies)

print(ratings)

nested_list = [list(t) for t in zip(movies,ratings)]
print(nested_list)

a = (min(ratings))

c = ratings.index(a)
#print(c)

movies.remove(movies[c])

ratings.remove(a)

print(movies)
print(ratings)


# In[61]:




