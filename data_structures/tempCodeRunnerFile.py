new_york = (40.7128, -74.0060)
denver = (39.7392, -104.9903)
austin = (30.2672, -97.7431)
seattle = (47.6062, -122.3321)

print(new_york)
print(denver)
print(austin)
print(seattle)

tuple_combine = print(f"{new_york} {denver} {austin} {seattle}")

if new_york > denver or austin or seattle:
  print("New York is the farthest")
elif denver > new_york or austin or seattle:
  print("Denver is the farthest")
elif austin > new_york or denver or seattle:
  print("Austin is the farthest")
elif seattle > new_york or denver or austin:
  print("Seattle is the farthest")
else:
  print("Error")
