#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Dog: 
    animal = 'dog'      # Class Variable      
    animal_type = 'mammal'
    
    def __init__(self, breed, color, age, charecteristic, sex):  # The init method or constructor      
        self.breed = breed  # Instance Variable
        self.color = color # Instance Variable
        self.age = age
        self.charecteristic = charecteristic
        self.sex = sex
    
    def print_breed(self):
        print(f'The breed of that dog is {self.breed}')
    
    def age_in_year(self, year):
        print(f"In {year} the dog was {self.age - (2021 - year)}")
    
    def print_charecteristic(self):
        print(f"One charecteristic of that dog is that it is {self.charecteristic}")
                
Zeus = Dog("Husky", "Silver", 9, "curious","male")
Hero = Dog("Corgi", "Burned peach",3, "playful", "male")
Zeus.print_charecteristic()


# In[ ]:


class MyTree:
    vascular_plant_type = 'tree'
    
    def __init__(self, tree_type, bark_color, bark_texture, height, avg_growth_per_year):
        self.tree_type = tree_type
        self.bark_color = bark_color
        self.bark_texture = bark_texture
        self.height = height
        self.avg_growth_per_year = avg_growth_per_year
    
    def print_height(self):
        print(f"The height of this tree is {self.height}")
        
    def future_height(self):
        int_height = int(self.height)
        int_growth = int(self.avg_growth_per_year)
        print(f"In 5 years, this tree will be {int_height + int_growth * 5}")

Tree_1 = MyTree("weeping willow", "grey", "rough", "35", "5")
Tree_2 = MyTree("cajeput", "white", "spongey", "25", "2")
Tree_1.future_height()

