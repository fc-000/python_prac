import random

health = 100
D_health = 100
choice = 0
player = 0

print("--(A Terminal Adventure Game)--")
print("A two headed dragon appeared!")
print("Fight or Flee?")
print("1) FIGHT")
print("2) Flee")
choice = int(input("choice: "))

while choice != 2: 
  if choice == 1:
    print("----------------------------")
    print("1) Slash")
    print("2) Heal")
    player = int(input("choice: "))
      

    if player == 1:
      D_health = D_health - 30
      print("------------}0{-------------")
      print("Player used Slash")
      print(f"Dragon's health: {D_health}")

    elif player == 2:
      health = health + 10
      print("----------------------------")
      print("player used 'Heal!'")
      print(f"Player health:{health}")

    dragon = random.randint (1, 2)

    if dragon == 1:
      health = health - 50
      print("-------------0--------------")
      print("Dragon dealth CRITICAL HIT!!")
      print(f"Player health: {health}")
    elif dragon == 2:
      health = health - 30
      print("-------------0--------------")
      print("Dragon scathed you.")
      print(f"Player health: {health}")
    else:
      print("erm, off script error.")

  elif choice == 2:
    print("Fleeing from the Dragon!!")


