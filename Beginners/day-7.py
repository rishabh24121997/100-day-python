word_list = [
"autumn", "prime", "headshot", "attack", "believe", "monsoon", "crime", "xenon", "welcome", "horrible", "camel", "love", "important", "summer", "cool", "sexy"
]

import random

chosen_word = random.choice(word_list)
n = len(chosen_word)
blank = ['_'] * n

lives = 6

while('_' in blank and lives > 0):
  guess = input("Guess a letter: ").lower()
  flag = 0
  for i in range(n):    
    if (chosen_word[i] == guess):
      blank[i] = guess
      flag = 1
  if(flag == 0):
      lives -= 1
  print(blank)
  print(f"Lives: {lives}")


if(lives == 0):
  print("You lost")
  print(f"The word was {chosen_word}")
else:
  print("You won")
