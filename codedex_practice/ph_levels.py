ph = int(input("give me a ph level bro (1-14): "))

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")