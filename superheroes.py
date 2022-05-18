#!/usr/bin/env python3

Freakzoid={'Real Name':'Remy LeBeau','First Appearance':'Uncanny X-Men Annual #14 (July, 1990), Uncanny X-Men #266 (August, 1990)','Creators':['Chris Claremont','Jim Lee'],'Team Affliations':['X-Factor','X-Men','Marauders','Horsemen of Apocalypse,'],'Base of Operations':'Salem Centre, New York'}

print(Freakzoid["Real Name"])
print(Freakzoid.get("Origin", "Sorry we dont have that information"))
print()
print("the challenge starts here*****************************")
print("original list: ", Freakzoid)
Freakzoid["fav_food"] = "bandeja paisa"
print("new list: ", Freakzoid)
print("")
print("all the keys: ", Freakzoid.keys())
choice = input("choice a key from the last line of code in order to see its value: ")
while choice not  in  Freakzoid.keys():
    choice = input("do it again...Read!!")
    if choice in Freakzoid.keys():
    
        break
    else: print( "are you reading the F instructions? try again")
print("Freakzoid ", choice, "is: ", Freakzoid[choice])   
