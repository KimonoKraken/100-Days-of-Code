############### Blackjack Project #####################

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import os
from art import logo

def clearConsole():
  """Clears the console as you play the game"""
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
  os.system(command)
    
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

  
def calculate_score(cards):
  """Takes a list of cards and calculates added score from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)  

  
def compare(user_score, computer_score):
  """Compares user's score with computer's score"""
  if user_score == computer_score:
    return "It's a draw.\n"
  elif computer_score == 0:
    return "You lose, computer hit blackjack!\n"
  elif user_score == 0: 
    return "You win with a blackjack!\n"
  elif user_score > 21:
    return "You went over, you lose!\n"
  elif computer_score > 21:
    return "Computer went over, you win!\n"
  elif user_score > computer_score:
    return "You win!\n"
  else:
    return "You lose.\n"


    

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  
  while is_game_over == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if user_score == 0:
      print(f"Your cards are {user_cards}. Blackjack!")
    else:
      print(f"Your cards are {user_cards}. Your score is {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or user_score > 21:
      is_game_over = True
    elif user_score == 0 and computer_score == 0:
      is_game_over = True
    else:
      user_should_deal = input("Do you want to 'hit' or 'stay'?: ").lower()
      if user_should_deal == "hit":
        clearConsole()
        print(logo)
        user_cards.append(deal_card())
      else:
        clearConsole()
        print(logo)
        is_game_over = True
  
  
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  if user_score == 0:
    print(f"Your final hand is {user_cards}, you hit Blackjack!") 
  else:
    print(f"Your final hand is {user_cards} for a total score of {user_score}.")  
  if computer_score == 0:
    print(f"Computer's final hand is {computer_cards}, dealer hit Blackjack!") 
  else:
    print(f"The computer's cards are {computer_cards} for a score of {computer_score}.")    
  
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clearConsole()
  play_game()
