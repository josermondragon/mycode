#!/usr/bin/env python3

vamp = 0

with open("dracula.txt","r") as foo:
    for line in foo:
        if "vampire" in line.lower():
            vamp +=1
            print(line)
            with open("vampytimes.txt", "a") as vampi:
               vampi.write(line +" \n")
print("the word vampire appears: ", vamp, " times in the book")
print("Check and Count if you want:\n "
