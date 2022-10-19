import random
import os
clear = lambda: os.system('cls')

def playeGame():
  dealer = []
  player = []
  is_game_over = False
  
  
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
  
  def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if sum(cards) > 21 and 11 in cards:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
  
  def compare(p,d):
    if p == d:
      return 'Draw'
    elif d == 0:
      return 'Lose'
    elif p == 0:
      return 'Win'
    elif p > 21:
      return 'Lose'
    elif d > 21:
      return 'Win'
    elif p > d:
      return 'Win'
    else:
      return 'Lose'
  
  
  for _ in range(2):
    dealer.append(deal_card())
    player.append(deal_card())
  
  while is_game_over == False:
    dealer_score = calc_score(dealer)
    player_score = calc_score(player)
  
    print(f"Your cards: {player}, score: {player_score}")
    print(f"Computer's first card: {dealer[0]}")
  
    if (dealer_score == 0 or player_score == 0 or player_score > 21):
      is_game_over = True
    else:
      user_should_deal = input(
        "Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_should_deal == 'y':
        player.append(deal_card())
      else:
        while dealer_score != 0 and dealer_score < 17:
          dealer.append(deal_card())
          dealer_score = calc_score(dealer)
  
    print(compare(player_score,dealer_score))
    result = input('Restart game: ')
    if(result == 'y'):
      clear()
      playeGame()


playeGame()