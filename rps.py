# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 09:20:14 2022

@author: wvarner3
"""
#0 is loose, tie is 1, win is 2
import random
import time
import os

choiceEnemy = "ROROAROWo"
scoreP = 0
scoreM = 0
choiceName = "null"
hands = ""


def RANDOM():
    return(random.randint(1, 3))

def enemyRoll():
    global enemy
    enemy = RANDOM()
    global hands
    global choiceEnemy
    #print(enemy)
    if enemy == 1:
        choiceEnemy = "rock"
        #print("rock")
    elif enemy == 2:
        choiceEnemy = "paper"
        #print("paper")
    elif enemy == 3:
        choiceEnemy = "scissors"
        #print("scissors")
def handStuff():      
    global choiceEnemy
    global enemy
    global choice
    global status
    global choiceName
    #print("Guess what",choiceEnemy)
    if choiceName == "rock":
        #print("IT SHOWS ROCK!")
        if enemy == 1:
            status = 1

            print ( """
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
            """)
        elif enemy == 2:
            status = 0
            print ( """
    _______                   _______  
---'   ____)             ____(____    '---
      (_____)          (_____) 
      (_____)          (_____) 
      (____)            (____)   
---.__(___)              (___________.---

__   __            _                         _ 
\ \ / ___  _   _  | |    ___   ___  ___  ___| |
 \ V / _ \| | | | | |   / _ \ / _ \/ __|/ _ | |
  | | (_) | |_| | | |__| (_) | (_) \__ |  __|_|
  |_|\___/ \__,_| |_____\___/ \___/|___/\___(_)
                                               
            """)
        elif enemy == 3:
            status = 2
            print ( """
    _______                   _______  
---'   ____)             ____(____    '---
      (_____)          (_____) 
      (_____)          (_____) 
      (____)                 (____)   
---.__(___)                  (____)_.---

 __   __           __        ___       _ 
 \ \ / ___  _   _  \ \      / (_)_ __ | |
  \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
   | | (_) | |_| |   \ V  V / | | | | |_|
   |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)
                                         
            """)

    elif choiceName == "paper":
        if enemy == 1:
            choiceEnemy ="rock"
            status = 3
            print ( """
     _______                  _______  
---'    ____)____           (____   '---
           ______)        (_____) 
          _______)        (_____) 
         _______)          (____)   
---.__________)             (___)__.---

 __   __           __        ___       _ 
 \ \ / ___  _   _  \ \      / (_)_ __ | |
  \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
   | | (_) | |_| |   \ V  V / | | | | |_|
   |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)
                                         
            """)
        elif enemy == 2:
            status = 1
            print( """
     _______                      _______  
---'    ____)____             ___(____   '---
           ______)         (_______ 
          _______)        (_________ 
         _______)          (_________   
---.__________)              (_________.---     
                             
            _____ _      _ 
           |_   _(_) ___| |
             | | | |/ _ \ |
             | | | |  __/_|
             |_| |_|\___(_)                            
            """)
        elif enemy == 3:
            choiceEnemy = "scissors"
            status = 1
            print( """
     _______                     _______  
---'    ____)____          _____(____   '---
           ______)        (_______ 
          _______)        (__________ 
         _______)               (____)
---.__________)                  (___)__.---    
                           
 __   __            _                         _ 
 \ \ / ___  _   _  | |    ___   ___  ___  ___| |
  \ V / _ \| | | | | |   / _ \ / _ \/ __|/ _ | |
   | | (_) | |_| | | |__| (_) | (_) \__ |  __|_|
   |_|\___/ \__,_| |_____\___/ \___/|___/\___(_)
                                                
            """)
    elif choiceName == "scissors":
        #print("ok we good?")
        if enemy == 1:
            choiceEnemy = "rock"
            status = 0
            print( """
    _______                 _______    
---'   ____)____           (____   '---
          ______)         (_____) 
       __________)        (_____) 
      (____)               (____)
---.__(___)                 (___)__.---

 __   __            _                         _ 
 \ \ / ___  _   _  | |    ___   ___  ___  ___| |
  \ V / _ \| | | | | |   / _ \ / _ \/ __|/ _ | |
   | | (_) | |_| | | |__| (_) | (_) \__ |  __|_|
   |_|\___/ \__,_| |_____\___/ \___/|___/\___(_)
                                                
            """)
        elif enemy == 2:
            choiceEnemy= "paper"
            status = 2
            print ( """
    _______                     ________     
---'   ____)____           ____(____    '---
          ______)         (______           
       __________)        (_______      
      (____)               (_______         
---.__(___)                  (__________.---
                              
 __   __           __        ___       _ 
 \ \ / ___  _   _  \ \      / (_)_ __ | |
  \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
   | | (_) | |_| |   \ V  V / | | | | |_|
   |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)
                                                                       
            """)
        elif enemy == 3:
            choiceEnemy = "scissors"
            status = 1
            print ( """
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
                 

            """)
        #print("HUGE DRAMA")
def score():
    print("        Current Score: ", scoreP, " - ", scoreM)


    
def showHands():
    #print("showhands formula which is BEFORE the hand show command, so they rolled a", choiceName)
    print("   You played :", choiceName, "\n   Enemy played :", choiceEnemy, "\n")
    
    
def prompt():
            print("""
          Choose your weapon:
              
              1. Rock   2. Paper   3. Scissors
          """)
    

def changeScore():
    global scoreP
    global scoreM
    global status
    if status == 0:
        print("You loose!")
        scoreM = scoreM + 1
    elif status == 1:
        print ("It's a tie!")
    elif status == 2:
        print ("You win!")
        scoreP = scoreP + 1
        
    

print("""
  ____            _      ____                         ____       _                        _ 
 |  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __  / ___|  ___(_)___ ___  ___  _ __ ___| |
 | |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__| \___ \ / __| / __/ __|/ _ \| '__/ __| |
 |  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |     ___) | (__| \__ \__ \ (_) | |  \__ \_|
 |_| \_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|    |____/ \___|_|___/___/\___/|_|  |___(_)
                                   |_|                                                      
                                  """)

while True:
    global choice
    global status
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
    
    print("Selected", choiceName )
    print(hand)
    #os.system('pause')
    print("\n" * 3)
    time.sleep(1)
    print("Rock... \n")
    time.sleep(.5)
    print("Paper... \n")
    time.sleep(.5)
    print("Scissors... \n")
    time.sleep(.5)
    print("Shoot!")
    enemyRoll()
    print("\n" * 2)
    handStuff()
    showHands()
    changeScore()
    os.system('pause')
    print("\n" * 50)
    score()