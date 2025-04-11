height = int(input("What is your height: "))
credits = int(input("What is your credit: "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You do not have enough credits.")
else:
  print("Sorry, you do not meet the requirements.")