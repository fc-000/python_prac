# April 4 2025 - Rock Paper Scissors Game
# Beginner - not the most efficient code
import random
choice = 0

while choice != 4:
  print("-----Rock Paper Scissors!-----")
  print("1) Rock")
  print("2) Scissors")
  print("3) Paper")
  choice = int(input("ur number: "))
  print("------------------------------")

  if choice == 1:
    print("your sign: 'Scissors'")
  elif choice == 2:
    print("your sign: 'Paper'")
  elif choice == 3:
    print("your sign: 'Rock'")
  elif choice == 4:
    print("Bye")
  else:
    print("invalid")

  bot = random.randint(1, 3)

  if bot == 1:
    bot = 1
    print("bot sign: 'Scissors'")
  elif bot == 2:
    bot = 2
    print("bot sign: 'Paper'")
  elif bot == 3:
    bot = 3
    print("bot sign: 'Rock'")
  else:
    print("ion even know what happened")
   
  # ik for a fact this aint efficient
  if bot == 1 and choice == 1:
    print("Tie")
  elif bot == 1 and choice == 2:
    print("You lost")
  elif bot == 1 and choice == 3:
    print("You won")
  elif bot == 2 and choice == 2:
    print("Tie")
  elif bot == 2 and choice == 3:
    print("You lost")
  elif bot == 3 and choice == 3:
    print("Tie")
  elif bot == 3 and choice == 1:
    print("You lost")
  elif bot == 2 and choice == 1:
    print("You won")
  elif bot == 3 and choice == 2:
    print("You won")
  else:
    print("Error")
  