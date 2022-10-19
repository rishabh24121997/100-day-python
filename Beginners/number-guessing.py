import random
import os
clear = lambda: os.system('cls')

def playGame():
  clear()
  print('Welcome to the number guessing game')
  print("I'm thinking of a number between 1 and 100")
  dif = input("Choose difficulty: 'easy' or 'hard': ")

  number = random.randint(1,100)
  if dif == 'easy':
    attempts = 10
  elif dif == 'hard':
    attempts = 5
    
  while(attempts > 0):
    val = int(input("Guess the number: "))
    if val > number:
      print("Too high")
      attempts -= 1
      if(attempts == 0):
        print('You lose')
        break
      print(f"Remaining attempts: {attempts}")
    elif val < number:
      print("Too low")
      attempts -= 1
      if(attempts == 0):
        print('You lose')
        break
      print(f"Remaining attempts: {attempts}")
    else:
      print(f"Yes, {val} is the number")
      break

  result = input("Play again? ").lower()
  if result == 'y':
    playGame()

playGame()