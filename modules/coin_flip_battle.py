# coin flip exercise - fc000 attempt

import random

sides = ["Heads", "Tails"]

p1_flips = random.choices(sides, k=3)
p1_points = p1_flips.count("Heads")
print("Player 1 flips:", p1_flips)


p2_flips = random.choices(sides, k=3)
p2_points = p2_flips.count("Heads")
print("Player 1 flips:", p1_flips)

print(f"Player 1 score: {p1_points}")
print(f"Player 2 score: {p2_points}")


if p1_points > p2_points:
  print("Player 1 wins!")
elif p2_points > p1_points:
  print("Player 2 wins!")
else:
  print("I's a Tie!")

'''
  introduced .count which is used to count 
  how many times a specific item appears
  in a list (or string)
'''
