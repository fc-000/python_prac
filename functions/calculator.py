# Calculator 🔢
# Codédex sample

'''
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def exp(a, b):
  return a ** b

print(add(3, 5))
print(subtract(7, 2))
print(multiply(4, 8))
print(divide(9, 3))
print(exp(2, 3))

'''

# fc000's attempt but with further tweaks

def add(a, b):
      return a + b
def subtract(a, b):
      return a - b
def multiply(a, b):
      return a * b
def divide(a, b):
      return a / b
def exp(a, b):
      return a ** b

while True:
  print("---Calculator---")
  a = float(input("Enter 1st number: "))
  b = float(input("Enter 2nd number: "))
  op = input("Add, subtract, multiply, divide, or exp? ")

  op = op.lower()

  if op == "add":
      print(add(a, b))
  elif op == "subtract":
      print(subtract(a,b))
  elif op == "multiply":
      print(multiply(a, b))
  elif op == "divide":
      print(divide(a, b))
  elif op == "exp":
      print(exp(a, b))
  else:
      print("invalid op")

  choice = input("Do another or exit program? ")
  choice = choice.lower()
  if choice == 'exit program':
      print("Thank you for using!")
      break