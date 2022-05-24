#!usr/bin/dev python3
import requests
from pprint import pprint
import json

#0:"back"
#1:"cardio"
#2:"chest"
#3:"lower arms"
#4:"lower legs"
#5:"neck"
#6:"shoulders"
#7:"upper arms"
#8:"upper legs"
#9:"waist"
print("WELCOME TO YOUR WORKOUT GENERATOR")
print("find a workout based on the muscle that you want to work the list of muscles is: ")


target = input("type muscle you want to workout\n>")
url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/"
full_url = url + target

headers = {
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com",
	"X-RapidAPI-Key": "ae3c4336c8mshcddd9bad47a4423p1e3161jsn67160c304656"
}

response = requests.request("GET",full_url, headers=headers)

#workdata = response.json()
#pprint(response.text)
#workoute = response.json()[i]["gifUrl"]
with open("workoutTest.txt","a") as work:
#print the gift of the exercises for the muscle selected
     i=0 
     for x in response.json():
        workoute = response.json()[i]["gifUrl"]
        work.write('\n'+target + '\nExercise link:\n') 
        rawjson = work.write(workoute)
        i +=1






                                                                     
                                                                     
                                                                     
                                                                     












