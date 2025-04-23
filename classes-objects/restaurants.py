# Codedex
# intro to classes-objects

'''
class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = True
'''

#fc000's attempt

class House:
  address = ''
  price = 0.0
  bedrooms = 0
  has_garden = True

house1 = House()
house2 = House()

house1.address = 'Somewhere'
house1.price = 400000
house1.bedrooms = 3
house1.has_garden = False

house2.address = 'Over the Rainbow'
house2.price = 500000
house2.bedrooms = 2
house2.has_garden = True

print(f"Address: {house1.address}, Price: {house1.price}, Bedrooms: {house1.bedrooms}, Has a Garden: {house1.has_garden}")