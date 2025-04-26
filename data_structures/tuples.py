new_york = (40.7128, -74.0060)
denver = (39.7392, -104.9903)
austin = (30.2672, -97.7431)
seattle = (47.6062, -122.3321)

print(f"New York:{new_york}, Denver:{denver}, Austin: {austin}, Seattle:{seattle}")


tuple_combine = (new_york, denver, austin, seattle)
print(tuple_combine)

farthest = max([new_york, denver, austin, seattle])

if farthest == new_york:
  print("New York is the farthest")
elif farthest == denver:
  print("Denver is the farthest")
elif farthest == austin:
  print("Austin is the farthest")
elif farthest == seattle:
  print("Seattle is the farthest")
else:
  print("There was an error.")

# Codedex solution

# Find My Friends 🙋🏽‍♀️
# Codédex

'''
# Task 1: Create Friends' Location Tuples
friend1_location = (37.7749, -122.4194) # San Francisco
friend2_location = (40.7128, -74.0060) # New York
friend3_location = (4.624335, -74.063644) # Bogota

# Bonus: Accessing Tuple Elements
print("Latitude and Longitude of the furthest friend's location:", friend1_location)

# Task 2: Tuple Operations
all_friends_locations = friend1_location + friend2_location + friend3_location

# Task 3: Print
print("All friends' locations combined:", all_friends_locations)

'''