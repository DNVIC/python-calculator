def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

a = 0
while a == 0:
  
  firstline = input("What is your first number: " )
  if is_number(firstline) == True:
    a = 1
    firstline = float(firstline)
  else:
    print("Please choose a number.")
    
    
def is_rightsign(i):
  if i == "*" or i == "x" or i == "+" or i == "-" or i == "/" or i == "÷" or i == "%":
    return True
  else:
    return False


b = 0
while b == 0: 
  symbol = input("What is your symbol (must be symbol): ")
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
  else:
    print("Please choose a number.")
  
def result(a,b,c):
  if b == "*" or b == "x":
    return a * c
  elif b == "+":
    return a + c
  elif b == "-":
    return a + c
  elif b == "/" or "÷":
    return a / c
  elif b == "%":
    return a % c
  else:
    print("There might have been an error in my coding")
print("Your equation is: " + str(firstline) + " " + str(symbol) + " " + str(secondline))
result = result(firstline, symbol, secondline)
print("Your result is: " + str(result))
