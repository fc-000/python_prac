import random

P_health = 100
D_health = 100
dmg = 0
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
      D_health = D_health - 70
      if D_health <= 0:
        D_health = 0
      print("WHAT THE SIGMA!!! CRITICAL HIT")
      print(f"Dragon's health: {D_health}")

    elif player == 2:
      P_health = P_health + 10
      print("----------------------------")
      print("player used 'Heal!'")
      print(f"Player health: {P_health}")


    dragon = random.randint (1, 3)

    if dragon == 1:
      P_health = P_health - 50
      if P_health <= 0:
        P_health = 0
      print("-------------0--------------")
      print("Dragon dealth CRITICAL HIT!!")
      print(f"Player health: {P_health}")
    elif dragon == 2:
      P_health = P_health - 30
      if P_health <= 0:
        P_health = 0
      print("-------------0--------------")
      print("Dragon scathed you.")
      print(f"Player health: {P_health}")
    elif dragon == 3:
      P_health = P_health - 0
      if P_health <= 0:
        P_health = 0
      print("-------------0--------------")
      print("Dragon missed!! crazy!!")
      print(f"Player health: {P_health}")
    else:
      print("erm, off script error.")  

    if P_health == 0:
      print("----------")
      print("You lost")
      break
    elif D_health == 0:
      print("----------")
      print("You won!")
    
  elif choice == 2:
    print("Fleeing from the Dragon!!")


