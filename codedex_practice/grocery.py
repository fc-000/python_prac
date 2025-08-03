# there was an attempt kay wala nakoy club membership HSHSHS
list = 0
items = 0

print("---Grocery List---")

for i in range(5):
  items += 1
  grocery_list = input("List your items: ")
  if i == 4:
    choice = input("Would you like to add more? (yes or no): ")
    if choice == "yes":
      items += 1
      grocery_list = input("List your items: ")
    if choice == "no":
      print(grocery_list)
  




