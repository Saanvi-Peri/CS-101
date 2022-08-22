#!/usr/bin/env python
# coding: utf-8

# In[95]:


class Monster:
    #time = "day"
    #bonus = -1
    time = input("Enter day or night: ")

    def __init__(self, a, b, c):
        self.level = 1
        self.ID = a
        self.HP = b
        self.power = c

    def __str__(self):
        return f"{self.ID}, {self.HP} hp, {self.power} power, level {self.level}"

    def __repr__(self):
        return self.__str__()

    def intro(self):
        print(self.__str__())
    
    #def getPower(self):
        #return self.power + Monster.bonus
    
    def setDay(self):
        #Monster.time = new_time
        if Monster.time == "day":
            bonus = -1
        if Monster.time == "night":
            bonus = 2
        return bonus
    
monster_101 = Monster("Monster 101", 6, 4)

monster_101.intro()
monster_102 = Monster("Fake Monster 102", "-8 hp", "-100")

Monster.setDay = classmethod(Monster.setDay)
Monster.setDay()

#print(monster_101.getPower())


# In[12]:




