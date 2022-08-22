#!/usr/bin/env python
# coding: utf-8

# In[7]:


season = ""

month = input("Pick a month")

if (month in ["March","April","May"]):
    season = "Spring"
if (month in ["June", "July", "August"]):
    season = "Summer"
if (month in ["September", "October", "November"]):
    season = "Fall"
if (month in ["January","February","December"] ):
    season = "Winter"
    
print(f"{month} - {season}")


# In[6]:


month = input("What is your birth month?")
day = input("What day were you born?")
if (month in ["4"])and(day in ["19","20","21","22","23","24","25","26","27","28","29","30"]):
    print("Your zodiac sign is Aries")
if (month in ["5"])and(day in ["1","2","3","4","5","6","7","8","9","10","11","12","13"]):
    print("Your zodiac sign is Areis")
if (month in ["5"])and(day in ["14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]):
    print("Your zodiac sign is Taurus")
if (month in ["6"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]):
    print("Your zodiac sign is Taurus")
if (month in ["6"])and(day in ["20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30"]):
    print("Your zodiac sign is Gemini")
if (month in ["7"])and (day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]):
    print("Your zodiac sign is Gemini")
if (month in ["7"])and(day in [ "21", "22", "23", "24", "25","26", "27", "28", "29", "30","31"]):
    print("Your zodiac sign is Cancer")
if (month in ["8"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
    print("Your zodiac sign is Cancer")
if (month in ["8"])and(day in ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25","26" "27", "28", "29", "30"]):
    print("You birth month is Leo")
if (month in ["9"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]):
    print("Your zodiac sign is Leo")
if (month in ["9"])and(day in ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30","31"]):
    print("Your zodiac sign is Virgo")
if (month in ["10"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30"]):
    print("Your zodiac sign is Virgo")
if (month in ["10"])and(day in ["31"]):
    print("Your zodiac sign is Libra")
if (month in ["11"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]):
        print("Your zodiac sign is Libra")
if (month in ["11"])and(day in ["23","24", "25","26", "27", "28", "29"]):
    print("Your zodiac sign is Scorpious")
if (month in ["11"])and(day in ["30"]):
    print("Your zodiac sign is Ophiuchus")
if (month in ["12"])and(day in ["1", "2", "3", "4","5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]):
    print("Your zodiac sign is Ophiuchus")
if (month in ["12"])and(day in ["18", "19", "20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30", "31"]):
    print("Your zodiac sign is Sagittarius")
if (month in ["1"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]):
    print("Your zodiac sign is Sagittarius")
if (month in ["1"])and(day in ["19", "20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30"]):
    print("Your zodiac sign is Capricorn")
if (month in ["2"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]):
    print("Your zodiac sign is Capricorn")
if (month in ["2"])and(day in ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30", "31"]):
    print("Your zodiac sign is Aquarius")
if (month in ["3"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]):
    print("Your zodiac sign is Aquarius")
if (month in ["3"])and(day in ["12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30"]):
    print("Your zodiac sign is Pisces")
if (month in ["4"])and(day in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]):
    print("Your zodiac sign is Pisces")
    


# In[12]:


year = input("Enter a year")   
if (year%4 == 0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")
elif (year%100 == 0):
    print("This is not a leap year.")


# In[ ]:




