#!/usr/bin/env python
# coding: utf-8

# In[48]:


class Character:
    def __init__(self, HP):
        self.HP = HP
        self.level = 1
    
    def universal_intro(self):
        print(f'The character is {self.__class__.__name__}')

class Monster(Character):
    time = 'day'
    bonus = -1
    def __init__(self, ID, HP, power):
        super().__init__(HP)
        self.ID = ID
        self.power = power
        self.bonus_power = self.power
        
    def intro(self):
        print(f"""Monster {self.ID}, {self.HP} hp, {self.bonus_power} power, and level {self.level}.""")

    def bonus_update(self):
        self.bonus_power = self.power + self.bonus
    
    def change_time(cls, time):
        if time == 'day':
            cls.time = 'day'
            cls.bonus = -1
        else:
            cls.time = 'night'
            cls.bonus = 2
    
    def level_adjust(self, hero_level, difficulty):
        if difficulty == 'easy':
            self.level = hero_level - 2
        if difficulty == 'hard':
            self.level = hero_level + 2
        else:
            self.level = hero_level

            
    
class Hero(Character):
    # class variables/attributes
    side = 'light'
    
    def __init__(self, HP, strength):
        super().__init__(HP)
        self.strength = strength
    
     # instance method
    def levelup(self, x):
        self.level += x 
        
     # instance method - introduction
    def intro(self):
            return(f"The hero has {self.HP} HP, and {self.strength} strength and is on level {self.level}")
        
        
    # class method
    def change_side(cls):
        if Hero.side == 'light':
            Hero.side = 'dark'
        else:
            Hero.side = 'light'

class NPC(Character):
    time = 'day'
    attitude = 'friendly'
    def __init__(self, HP, level, ID, num_coins, health_potion):
        self.HP = HP
        self.level = level
        self.ID = ID
        self.num_coins =num_coins
        self.health_potion = health_potion
    
    def introd(self):
        if NPC.attitude == 'friendly':
            print(f"""ID = {self.ID}, wealth = {self.num_coins}, bag content = {self.health_potion}""")
        else:
            print("Monster has refused to say.")
            
    def day_or_night(time):
        if NPC.time == "day":
            NPC.attitude = "friendly"
        if time == "night":
            NPC.attitude = "hostile"
        if NPC.attitude == "friendly":
            print([f"The HP is 5, the level is 1, and the ID is 3749"])
        else:
            print("Since you are hostile, you will not be getting a message you monster.")
monstr = Monster(66, 79, 9000)
hero = Hero(99, 120)
hero.intro()
monstr.intro()
monstr.bonus_update()
monstr.intro()
Monster.change_time(Monster, 'night')
print('***Sunset***')
monstr.bonus_update()
monstr.intro()
monstr.level_adjust(hero.level, 'hard')
monstr.intro()
introduction = NPC(54, 1, 688, 20, "bandage")
introduction.introd()
introduction.day_or_night(NPC, "day")


# In[33]:


class NPC():
    time = 'day'
    attitude = 'friendly'
    def __init__(self, HP, level, ID, num_coins, health_potion):
        self.HP = HP
        self.level = level
        self.ID = ID
        self.num_coins =num_coins
        self.health_potion = health_potion
    
    def intro(self):
            return(f"ID is {self.ID}, wealth is {self.num_coins}, bag content is {self.health_potion}")

introduction = NPC(54, 1, 688, 20, "bandage")
introduction.intro()

