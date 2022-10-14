def ceaser(text,shift,direction):
  newText = ''
  if(direction == 'decoded'):
    shift = -1 * shift
  for l in text:
    pos = ord(l) - 97
    if(pos > 0 and pos < 26):      
      change = (pos + shift)%26 + 97
      newL = chr(change)
    else:
      newL = l
    newText += newL

  print(f"The {direction} text is {newText}")


should_continue = True
while(should_continue == True):
  direction = input('Type "encoded" to encrypt, type "decoded" to decrypt: \n: ')
  text = input('Type your message: \n').lower()
  shift = int(input("Type your shift number: \n"))
  ceaser(text,shift,direction)
  result = input("'Y' to continue and 'N' to end: \n")
  if result == 'n':
    should_continue = False
# vmwlafl wlavqa