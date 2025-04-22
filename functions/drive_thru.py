# Drive-Thru 🚙
# Codédex Sample

'''
def get_item(x):
  if x == 1:
    return '🍔 Cheeseburger'
  elif x == 2:
    return '🍟 Fries'
  elif x == 3:
    return '🥤 Soda'
  elif x == 4:
    return '🍦 Ice Cream'
  elif x == 5:
    return '🍪 Cookie'
  else:
    return "invalid option"

def welcome():
  print('Welcome to Sonnyboy\'s Diner!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))

'''

# fc000's attempt
def get_pizza(x):
  if x == 1:
    return '🧀 Cheese Pizza'
  elif x == 2:
    return '🍖 Pepperoni Pizza'
  elif x == 3:
    return '🍄 Mushroom Pizza'
  elif x == 4:
    return '🌶️ Spicy Jalapeño Pizza'
  elif x == 5:
    return '🍍 Hawaiian Pizza'
  else:
    return "That's not on the menu, sorry."
    
def greet_customer():
  print("Hi welcome to Freddie Fazdogs Pizza")
  print("1. 🧀 Cheese Pizza ")
  print("2. 🍖 Pepperoni Pizza")
  print("3. 🍄 Mushroom Pizza")
  print("4. 🌶️ Spicy Jalapeño Pizza")
  print("5. 🍍 Hawaiian Pizza")

greet_customer()

choice = int(input("What pizza would you like? (Enter a number): "))
print(get_pizza(choice))