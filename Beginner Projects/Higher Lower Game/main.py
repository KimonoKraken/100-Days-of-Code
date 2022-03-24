
import random
from game_data import data
from art import logo, vs
import os


#generate random social media account from game_data file
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

#clears screen
def clearConsole():
  """Clears the console as you play the game"""
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
  os.system(command)
  
#format account data into printable format
def format_data(account):
  account_name = account["name"]
  account_descrip = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descrip} from {account_country}"

#checks users guess vs which account has more followers
def check_answer(guess, a_followers, b_followers):
  """takes users guess, follower counts, and checks if user was correct"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


#game starts
print(logo)
user_score = 0
continue_game = True

while continue_game == True:
  #makes 2nd account go to 1st account place to avoid predictable game
  account_a = account_b
  account_b = random.choice(data)
  print(f"\nCompare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
       
    
  #asks user to guess who has more followers
  guess = input("Who has more followers? 'A' or 'B': ").lower()
  
  #check users answer see if user is correct
  #gets follower number from each account
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
 
  
  clearConsole()
  print(logo)
  
  #gives user feedback on their guess
  if is_correct == True:
    user_score += 1
    print(f"You guessed right! Your score is {user_score}.")
    
  else:
    print(f"Sorry, that's not right. Your final score is {user_score}.")
    continue_game = False
