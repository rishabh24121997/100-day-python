from art import logo, vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')

def playGame():
  clear()
  print(logo)
  game_over = False
  score = 0
  n = len(data)
  a = data[random.randint(0,n-1)]
  b = data[random.randint(0,n-1)]
  while(b == a):
    b = data[random.randint(0,n-1)]

  while game_over == False:
    clear()
    if(score != 0):
      print(f"That's right. Current score: {score}")
      
    print(f"A: {a['name']}, a {a['description']}, from {a['country']} ")

    print(vs)
  
    print(f"B: {b['name']}, a {b['description']}, from {b['country']} ")
  
    result = input("Who has more followers? Type 'a' or 'b': ").lower()
    while(result != 'a' and result != 'b'):
      result = input("Wrong input. Please enter again: ").lower()
  
    if((result == 'a' and a['follower_count']<b['follower_count']) or (result == 'b' and a['follower_count']>b['follower_count'])):
      clear()
      print(f"Sorry, you're wrong. Final score: {score}")
      game_over = True
    else:
      score += 1
      if(result == 'a'):
        b = data[random.randint(0,n-1)]
        while(b == a):
          b = data[random.randint(0,n-1)]
      else:
        a = b
        b = data[random.randint(0,n-1)]
        while(b == a):
          b = data[random.randint(0,n-1)]

  again = input("Would you like to play again? ").lower()
  if(again == 'y'):
    playGame()

playGame()
