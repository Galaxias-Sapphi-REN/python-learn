#!/usr/bin/python
# encoding: utf-8
import random
num = random.randint(1, 99)
print(''' Welcome to the magic python world !
 I've prepared a magic party for you.
 ''')

guess_num = int(input(" now guess a number (1 - 99) untill correct or enter 0 to exit!!\n"))

if guess_num == 0:  
    exit(0)

while guess_num != num:
    if guess_num == 0:
        exit(0)
    guess_num = int(input(" oh! too " + ("large" if guess_num > num else "small") +
                          "! continue or enter 0 to exit!:\n"))

print ("Congratulations my boy! u r all right! ")
