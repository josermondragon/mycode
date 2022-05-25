#!usr/bin/dev python3i
import requests
from pprint import pprint
import json
import random

print("WELCOME TO YOUR WORKOUT GENERATOR")
print('''find a workout based on the muscle that you want to workout
the list of muscles is:
back
chest
lower arms
upper arms
lower legs
upper legs
shoulders
waist
''')

j=1
def wrongInput():
    print("NO a valid entry:\n>")
    target= input(f"Please type the muscle {j}:\n>").lower()
    

muscleList = ["back","chest","lower arms","upper arms","lower legs","upper legs","shoulders","waist"]
#select 3 muscles and 4 exercises for each

for j in range (1,4):
   target = input(f"type muscle {j}  you want to workout\n>").lower()
   while target not in muscleList:
       try:
          if str(target)==str(target):
            wrongInput()
            target = False
            
       except:
           wrongInput()
           break
       else:
           wrongInput()
           break
   target = input(f"PLEASE CONFIRM THE MUSCLE {j}\n>").lower() 

   url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/"
   full_url = url + target

   headers = {
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com",
	"X-RapidAPI-Key": "ae3c4336c8mshcddd9bad47a4423p1e3161jsn67160c304656"
}

   response = requests.request("GET",full_url, headers=headers)
   jsonObj = response.json()

#write in a .txt file a work out with 4 random exercises of the muscles selected.
   with open("workoutTest.txt","a") as work:
#print in .txt name, equipment necessary and the link-gift of the exercises for the muscle selected 
         a = random.randint(1,10)
         i = a
         for x in jsonObj:
            if i == (a+4):
              break
            exercise = jsonObj[i]["gifUrl"]
            equipment = jsonObj[i]["equipment"]
            work.write('\n'+target + '\nExercise link:\n')
            rawjson = work.write(exercise + "\nequipment: " + equipment)
            work.write("\n")
            i +=1 
j +=1                                         
                                                                     
print("your workout is ready: ")
workoutTest = open("workoutTest.txt", "r")
## display file to the screen - .read()
print(workoutTest.read())
## close file
workoutTest.close()











