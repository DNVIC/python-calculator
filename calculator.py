import math
import click
def result(a,b,c):
   if b == "*" or b == "x" or b == "times" or b == "multiply":
     return a * c
   elif b == "+" or b == "plus" or b == "add":
     return a + c
   elif b == "-" or b == "subtract" or b == "minus":
     return a - c
   elif b == "/" or b == "÷" or b == "divide":
     return a / c
   elif b == "%" or b == "modulo" or b == "mod":
      return a % c
   elif b == "^":
      return a ** c
   elif b == "root":
     return a ** (1/c)
   else:
     print("There might have been an error in my coding. Error Code 1")
def is_rightsign(i):
  if i == "*" or i == "times" or i == "multiply" or i == "x" or i == "+" or i == "plus" or i == "add" or i == "-" or i == "subtract" or i == "minus" or i == "/" or i == "÷" or i == "divide" or i == "%" or i == "modulo" or i == "mod" or i == "^" or i == "root" :
    return True
  else:
    return False
def ifint(n):
  if n.is_integer() == True:
    return int(n)
  else:
    return n

doesend=0
while doesend == 0:
  firstline = click.prompt('What is your first number',type=float)   
  dingdong=0
  while dingdong == 0:
  
    b = 0
    while b == 0: 
      symbol = input("What is your symbol: ")
      if is_rightsign(symbol) == True:
        b = 1
      else: 
       print("Wrong input, please try again.")

    secondline = click.prompt('What is your second number',type=float)

  
    print("Your equation is: " + str(ifint(firstline)) + "  " + str(symbol) + " " + str(ifint(secondline)))
    theresult = result(firstline, symbol, secondline)
    print("Your result is: " + str(ifint(theresult)))
    if click.confirm('Do you want to continue?') == False:
      doesend = 1
      break

    if click.confirm('Do you want to operate on your previous number?'):
      firstline = theresult
      dingdong = 0
    else:
      dingdong = 1

