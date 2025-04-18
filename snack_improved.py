# snacks improved version 

snacks = ["peanuts",
          "pan de sal",
          "jolly",
          "breadstix"
          ]

print(f"Snacks available: {snacks}")

while True:
  choice = int(input("How many do you want to bring? "))

  if choice == 0:
    print(f"You don't want snacks??")
    break
  elif 1 <= choice <= len(snacks):
    print(f"You will bring {choice} snacks!")
  elif choice > len(snacks):
    print("Too many snacks!")
    print(f"you can only bring {len(snacks)} snacks!")