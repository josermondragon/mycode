#!/usr/bin/python3

import os
import time




# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' , str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' , rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms  **********JOSE: ADD THREE MORE ROOMS: GARAGE(with justagun), STORAGE(with ammo) and SECRET PASSAGE(with a way straight to the GARDEN), a MSG in garden and MILK FOR THE COOKIES IN PANTRY**********
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'north' : 'Storage',
                  'west'  : 'Garage',
                  'item'  : ['key'],
                  
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : ['potion'],
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'msg'   : 'If you could not escape at this point, go back and get the potion and keys... see you soon',
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : ['cookie','milk']
            },
            'Garage' : {
                  'east' : 'Hall',
                  'north': 'Storage',
                  'item' : ['justagun'],
            },
            'Storage' : {
                  'south' : 'Garage',
                  'east'  : 'Secret-Pass',
                  'item'  : ['ammo'],
                  
            },
            'Secret-Pass' : {
                  'south' : 'Garden',
            }

         }


#start the player in the Hall
currentRoom = 'Hall'


#os.system('clear') # clear the screen

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

#if they type 'go' first
  if move[0] == 'go':
      #check that they are allowed wherever they want to go ********** JOSE: YOU CAN GO JUST ONCE FROM HALL TO STORAGE.**********
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
       currentRoom = rooms[currentRoom][move[1]]
       try:
           if currentRoom == 'Storage'and rooms['Hall']['north'] != None:
             del rooms['Hall']['north']
             print("you cannot comeback this way")
       except:
            if move[1] in rooms[currentRoom]:
              #set the current room to the new room
              currentRoom = rooms[currentRoom][move[1]]

    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
  





  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      del rooms[currentRoom]['item'][0]      
      #**************JOSE: HAVE TWO ITEMS OR MORE *******************
      #Delete the elements when you took them
      print(move[1], ' got them!')
           
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
          
  
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  #**********JOSE: MESSAGE TO EXPLAIN WHAT TO GET IN ORDER TO ESCAPE********** 
  elif currentRoom == 'Garden':
      print(rooms[currentRoom]['msg'])
  #*********JOSE: IG YOU GOT THE GUN AND AMMO YOU CAN SHOT THE MONSTER AND SURVIVE**********
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'justagun' in inventory and 'ammo' in inventory:
      print('You shot the Monster 17 times... RUN NORTH')

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
