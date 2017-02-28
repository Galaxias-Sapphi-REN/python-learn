#!/usr/bin/python
# encoding: utf-8
"""
Created on 2017-1-19

@author: sapphire

cua 猜数字小游戏
"""
import random
num = random.randint(1, 99)
print('''
Welcome to the magic python world !
I've prepared a magic party for you.
 ''')

guess_num = int(input("Enter a number (1 - 99) to guess untill it\'s correct ( 0 to exit ) : "))

if guess_num == 0:
    exit(0)

while guess_num != num:
    if guess_num == 0:
        exit(0)
    guess_num = int(input("oh! too " + ("large" if guess_num > num else "small") +
                          "! continue or enter 0 to exit!:\n"))

print ("Congratulations my boy! you are right! ")
