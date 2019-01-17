import Math

def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def ifint(n):
    if n.is_integer() == True:
        return int(n)
    else:
        return n



a = 0
while a == 0:
  
  firstline = input("What is your first number: " )
  if is_number(firstline) == True:
    a = 1
    firstline = float(firstline)
  elif:
    if firstline == "e":
    a = 1
    firstline = Math.E
  elif:
    if firstline == "pi":
    a = 1
    firstline = Math.PI
  else:
    print("Please choose a number.")
    
    
def is_rightsign(i):
  if i == "*" or i == "times" or i == "multiply" or i == "x" or i == "+" or i == "plus" or i == "add" or i == "-" or i == "subtract" or i == "minus" or i == "/" or i == "÷" or i == "divide" or i == "%" or i == "modulo" or i == "mod" or i == "^" or i == "root" :
    return True
  else:
    return False


b = 0
while b == 0: 
  symbol = input("What is your symbol: ")
  if is_rightsign(symbol) == True:
    b = 1
  else: 
    print("Wrong input, please try again.")

c = 0
while c == 0:
  
  secondline = input("What is your second number: " )
  if is_number(secondline) == True:
    c = 1
    secondline = float(secondline)
  elif:
    if firstline == "e":
    c = 1
    secondline = Math.E
  elif:
    if firstline == "pi":
    c = 1
    secondline = Math.PI
  else:
    print("Please choose a number.")
  
def result(a,b,c):
  if b == "*" or b == "x" or b == "times" or b == "multiply":
    return a * c
  elif b == "+" or b == "plus" or b == "add":
    return a + c
  elif b == "-" or b == "subtract" or b == "minus":
    return a + c
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
print("Your equation is: " + str(ifint(firstline)) + " " + str(symbol) + " " + str(ifint(secondline)))
result = result(firstline, symbol, secondline)
print("Your result is: " + str(ifint(result)))
