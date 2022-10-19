import os
clear = lambda: os.system('cls')

def add(a,b):
  return a+b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

def subtract(a,b):
  return a-b


operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/':divide
}

def calculator():  
  clear()
  continue_code = True
  num1 = float(input('Whats the first number: '))
  while continue_code == True:
    num2 = float(input('Whats the second number: '))
    for symbol in operations:
      print(symbol)
    operation_symbol = input('Select an operation: ')
    cal_func = operations[operation_symbol]
    answer = cal_func(num1,num2)
    print(f'{num1} {operation_symbol} {num2} = {answer}')
  
    result = input('Do you wish to continue? ').lower()
    if result == 'n':
      continue_code = False
      calculator()
    else:
      num1 = answer

calculator()