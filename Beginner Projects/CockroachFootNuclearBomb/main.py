cockroach = r'''
   .--.   .--.
       \ /
       oVo
   \___XXX___/
    __XXXXX__
   /__XXXXX__\
___/   XXX   \___
        V
'''

foot = r'''
 ^^^^( )
|      |  
|     / 
|    (  
|     )   
 \___/          
'''

bomb = r'''
          ._  . _
       _ ._  _ , _ ._
     (_ ' ( `  )_  .__)
   ( (  (    )   `)  ) _)
  (__ (_   (_ . _) _) ,__)
      `~~`\ ' . /`~~`
           ;   ;
           /   \
__________/_ __ \_____________
'''

wrong = r'''
                           ||||||
                           | o o |
                           |  >  |
                           | \_/ |
                            \___/
                           __| |__
                          /       \
                         | |     | |
        _________________| |     | |_____________---__
       /                 | |_____| |         /  /  / /|
      /                  /_|  _  |_\        /  /  / / |
     /                    / / / /          /  /__/ / /|
    /____________________/ / / /__________/___\_/_/ / |
    |____________________| |_| |__________________|/  |
    |____________________| |_| |__________________|   /
____|              |     | | | | ||               |  /
    | o          o | o         o || o           o | /
    |______________|_____________||_______________|/
_______________________________________________________
'''

#Write your code below this line 👇
import random

options_list = ["0", "1", "2"]

#user's manual input
user_input = input("What do you choose? Type 0 for Cockroach, 1 for Foot, or 2 for Nuclear Bomb.\n").lower()
if user_input == "0":
  print(cockroach)
elif user_input == "1":
  print(foot)
elif user_input == "2":
  print(bomb)
else:
  print("You had 3 options to choose from... and you even messed that up!")
  print(wrong)
  exit(0)


print("\nComputer chose:\n")


#computer random select
computer_random = random.choice(options_list)
if computer_random == "0":
  print(cockroach)
elif computer_random == "1":
  print(foot)
elif computer_random == "2":
  print(bomb)

#Outcomes for victory/loss
if computer_random == "0" and user_input == "0":
  print("It's a draw!")
if computer_random == "0" and user_input == "1":
  print("You win!")
if computer_random == "0" and user_input == "2":
  print("You lost!")
if computer_random == "1" and user_input == "0":
  print("You lost!")
if computer_random == "1" and user_input == "1":
  print("It's a draw!")
if computer_random == "1" and user_input == "2":
  print("You win!")
if computer_random == "2" and user_input == "0":
  print("You win!")
if computer_random == "2" and user_input == "1":
  print("You lost!")
if computer_random == "2" and user_input == "2":
  print("It's a draw!")
