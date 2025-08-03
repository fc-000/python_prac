# .append exercise - Shopping List [fc000's attempt]

shopping_list = []

print("---Shopping List---") 
while True:
  item = input("What item would you like to add?  ")

  if item.lower() == "done": # converts a string to lowercase letters
    break

  shopping_list.append(item)
  print("Added to your list!")

print("Your shopping list: ") #prints shopping list
for product in shopping_list:
  print("- " + product)


