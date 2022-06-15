# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 09:20:14 2022

@author: wvarner3
"""

import random
import time
import os

def RANDOM():
    return(random.randint(1, 3))

scoreP = 0
scoreM = 0
choice = 0
enemy = 11
choiceEnemy = "choice enemy"
choiceName = "null"
hands = ""

def enemyRoll():
    enemy = RANDOM()
    print(enemy)
    
    
def score():
    print("        Current Score: ", scoreP, " - ", scoreM)


    
def showHands():
    print(hands)
    print("You played", choiceName, "cpu played", choiceEnemy)
    
    
def prompt():
            print("""
          Choose your weapon:
              
              1. Rock   2. Paper   3. Scissors
          """)
    

print("""
░█▀▄░█▀█░█▀▀░█░█░░░█▀█░█▀█░█▀█░█▀▀░█▀▄░░░█▀▀░█▀▀░▀█▀░█▀▀░█▀▀░█▀█░█▀▄░█▀▀
░█▀▄░█░█░█░░░█▀▄░░░█▀▀░█▀█░█▀▀░█▀▀░█▀▄░░░▀▀█░█░░░░█░░▀▀█░▀▀█░█░█░█▀▄░▀▀█
░▀░▀░▀▀▀░▀▀▀░▀░▀░░░▀░░░▀░▀░▀░░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
                                  """)

while True:
    score()
    prompt()
    choice = input("Enter choice(1/2/3): ")
    print("\n")
    
    if choice == '1':
        choiceName = "rock"
        hand = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        """
    elif choice == '2':
        choiceName = "paper"
        hand = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)        
        """
    elif choice == '3':
        choiceName = 'scissors'
        hand= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        """
    enemyRoll()        
        #enemy stuff below vvvvv
        
    if choice == 1:
        if enemy == 1:
            choiceEnemy = "rock"
            hands = """
    _______               _______  
---'   ____)             (____   '---
      (_____)          (_____) 
      (_____)          (_____) 
      (____)            (____)   
---.__(___)              (___)__.---

            _____ _      _ 
           |_   _(_) ___| |
             | | | |/ _ \ |
             | | | |  __/_|
             |_| |_|\___(_)
            """
        elif enemy == 2:
            choiceEnemy = "paper"
            hands = """
    _______                   _______  
---'   ____)             ____(____    '---
      (_____)          (_____) 
      (_____)          (_____) 
      (____)            (____)   
---.__(___)              (___________.---
            """
        elif enemy == 3:
            choiceEnemy = "scissors"
            hands = """
    _______                   _______  
---'   ____)             ____(____    '---
      (_____)          (_____) 
      (_____)          (_____) 
      (____)                 (____)   
---.__(___)                  (____)_.---
            """
        print(choiceEnemy)
    if choice == '2':
        if enemy == '1':
            choiceEnemy ="rock"
            hands = """
     _______                  _______  
---'    ____)____           (____   '---
           ______)        (_____) 
          _______)        (_____) 
         _______)          (____)   
---.__________)             (___)__.---
            """
        elif enemy == '2':
            choiceEnemy ="paper"
            hands= """
     _______                      _______  
---'    ____)____             ___(____   '---
           ______)         (_____) 
          _______)        (_____) 
         _______)          (____)   
---.__________)              (_________.---     
                             
            _____ _      _ 
           |_   _(_) ___| |
             | | | |/ _ \ |
             | | | |  __/_|
             |_| |_|\___(_)                            
            """
        elif enemy == '3':
            choiceEnemy = "scissors"
            hands= """
     _______                     _______  
---'    ____)____          _____(____   '---
           ______)        (_______ 
          _______)        (__________ 
         _______)               (____)
---.__________)                  (___)__.---           
            """
    print(hands)
    if choice == '3':
        if enemy == '1':
            choiceEnemy = "rock"
            hands= """
    _______                 _______    
---'   ____)____           (____   '---
          ______)         (_____) 
       __________)        (_____) 
      (____)               (____)
---.__(___)                 (___)__.---
            """
        elif enemy == '2':
            choiceEnemy= "paper"
            hands = """
    _______                     ________     
---'   ____)____           ____(____    '---
          ______)         (______           
       __________)        (_______      
      (____)               (_______         
---.__(___)                  (__________.---
            """
        elif enemy == '3':
            choiceEnemy = "scissors"
            hands = """
    _______                      _______     
---'   ____)____           _____(____   '---
          ______)         (_______                 
       __________)        (__________       
      (____)                    (____)      
---.__(___)                      (___)__.---

            _____ _      _ 
           |_   _(_) ___| |
             | | | |/ _ \ |
             | | | |  __/_|
             |_| |_|\___(_)
                 

            """
            
            

            
            
            
    print("Selected", choiceName )
    print(hand)
    os.system('pause')
    print("\n" * 3)
    time.sleep(1)
    print("Rock... \n")
    time.sleep(.5)
    print("Paper... \n")
    time.sleep(.5)
    print("Scissors... \n")
    time.sleep(.5)
    print("Shoot!")
    print("\n" * 2)
    showHands()  