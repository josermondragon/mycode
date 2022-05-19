#!/usr/bin/dev python3
import math
import time

#This app will calculate your caloric Expenditure approx.
print("CALORIC EXPENDITURE CALCULATOR")

# first question name
name = input("Please type your name: ")
if not name:
    print("ok lets keep your name secret, no problem...")
# second question age, is requiered and need to be only a number
age = input("Please type your age: ")

while age == "":
    print("your age is NEEDED!")
    age = input("lets try again..type your age: ")
    
while age:
    try:
      int(age) == int(age)
      age = False
  
    except ValueError:
        print("you need to type your holy age using INTEGER NUMBERS!")
        age = input("lets try again..type your age: ")
age=input("please confirm your age one more time: ")

# third question level factor ALF. just accept 4 numeric values no empty space allowed
print("Please Check and Type the Number Associate To Your Activity Level Factor-ALF")
print('''1 for Sedentary: little or not exercise
        \n2 for Lightly Active: exercise 1 - 3 times/week
        \n3 for Moderate Active: exercise 3 - 5 times/week
        \n4 for Very Active: exercise 6 - 7 times/week''')
alf = input("Type 1, 2, 3 or 4: ")
while not alf:
    print("white space omfg? Select a number between 1 and 4")
    alf = input("lets try again..type your ALF: ")

while alf:
    try:
       if int(alf)==int(alf) and int(alf)>0 and int(alf)<5:
          print("perfect...lets go on")
          alf = False     
    except ValueError:
            print("are you serious? Type a number between 1 and 4")
            alf = input("lets try again..type your ALF: ")
    else:
        if int(alf)>4:
                print("you need to type your Funny ALF  using NUMBERS 1,2,3 or 4")
                alf = input("lets try again..type your ALF: ")
alf=input("please confirm your alf one more time: ")

#fourth question height in inches I will change it to cm
height = input("type your height in INCHES: ")

while height == "":
    print("your height is NEEDED!")
    height = input("lets try again..type your height in INCHES: ")

while height:
    try:
        int(height) == int(height)
        height = False
  
    except ValueError:
        print("NO Again, type your Furios height using INTEGER NUMBERS!")
        height = input("lets try again..type your height..please INCHES: ")
height=input("please confirm your height one more time: ")

#fifth question weight in pounds I will converted to Kg
weight = input("type your weight in POUNDS: ")

while weight == "":
    print("your weight is NEEDED!")
    weight = input("lets try again..type your weight in POUNDS: ")

while weight:
    try:
      int(weight) == int(weight)
      weight = False

    except ValueError:
        print("A lo bien???, type your Fascinating  weight using INTEGER NUMBERS!")
        weight = input("lets try again..type your weight..please POUNDS: ")
weight=input("please confirm your weight one more time: ")

#CALCULATIONS
#alf
if alf == "1":
    alfn = 1.2
elif alf == "2":
    alfn = 1.375
elif alf == "3":
    alfn = 1.550
elif alf == "4":
    alfn = 1.725

#weight on POUNDS to KG
wKG = float(weight)/2.205

#height on INCHES to cm
hCM = float(height)*2.54

#caloric expenditure CE
ce =float(float(alfn)*((13.75*wKG)+(5*hCM)-(6.76*float(age))+66))

# print results
print(f"Ok {name}, lets check your result...")
time.sleep(1)
print("...working on it...")
time.sleep(2)
print("almost there..this is not duck #8")
time.sleep(3)
print("your CE or caloric expenditure is aproximately: ", int(ce) , " Calories per day")
