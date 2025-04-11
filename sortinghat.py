# April 5, 2025
# notes: didn't teach functions yet but this program legit calls for it
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer = int(input("answer: "))


gryff = 0
raven = 0
huffl = 0
slyth = 0

if answer == 1:
  gryff = gryff + 1
  raven = raven + 1
elif answer == 2:
  huffl = huffl + 1 
  slyth = slyth + 1
else:
  print("wrong input")

print("Q2) When I'm dead, I want people to remember me as: ")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer = int(input("answer: "))

if answer == 1:
  huffl = huffl + 2
elif answer == 2:
  slyth = slyth + 2
elif answer == 3:
  raven = raven + 2
elif answer == 4:
  gryff = gryff + 2
else:
  print("wrong input")

print("Q2) What kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer = int(input("answer: "))

if answer == 1:
  slyth = slyth + 4
elif answer == 2:
  huffl = huffl + 4
elif answer == 3:
  raven = raven + 4
elif answer == 4:
  gryff = gryff + 4
else:
  print("wrong input")

print(f'Gryff: {gryff}')
print(f'Raven: {raven}')
print(f'Hufflepuff: {huffl}')
print(f'Slytherin: {slyth}')

if gryff >= 4:
  print("Gryffindor has the most points!")
elif raven >= 4:
  print("Ravenclaw has the most points!")
elif huffl >= 4:
  print("HufflePuff has the most points!")
elif slyth >= 4:
  print("Slytherin has the most points!")