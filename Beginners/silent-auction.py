import os
clear = lambda: os.system('cls')

bid_dict = []

existing_players = True

while(existing_players == True):
  clear()
  name = input('Name: ')
  bid = int(input('Bid: Rs.'))
  new = {}
  new["name"] = name
  new["bid"] = bid
  bid_dict.append(new)
  result = input('Are there more bidders: ').lower()
  if(result == 'n'):
    existing_players = False

max = 0
player = ''
for e in bid_dict:
  if(e["bid"] > max):
    max = e["bid"]
    player = e["name"]

clear()
print(f'The highest bidder is {player} and the bid is Rs. {bid}')

