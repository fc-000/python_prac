# snacks list exercise - fc000's attempt

snacks = ["peanuts",
          "pan de sal",
          "jolly",
          "breadstix"
          ]

print(f"Snacks available: {snacks}")

choice = ""

while choice != 0:
   
  choice = int(input("How many do you want to bring? "))

  if choice == 1:
    print(f"You will bring", (choice), "snacks")
  elif choice == 2:
    print(f"You will bring", (choice), "snacks")
  elif choice == 3:
    print(f"You will bring", (choice), "snacks")
  elif choice == 4:
    print(f"You will bring", (choice), "snacks")
  elif choice > 4:
    print("Too many snacks!")
    print("you can only bring", len(snacks), "snacks!")
  elif choice == 0:
    print("You don't want snacks??")

