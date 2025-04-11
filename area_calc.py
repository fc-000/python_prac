while type != 5:
  print("---------------------")
  print("Area Calculator")
  print("Please input a number")
  print("1) Circle")
  print("2) Triangle")
  print("3) Rectangle")
  print("4) Square")
  print("5) Exit")
  type = int(input("number: "))

  if type == 1: #Circle
    print("---Area of Circle---")
    r = int(input("radius: "))
    print(f"Formula: 3.14 * {r} * 2")
    area = 3.14 * r ** 2
    print(f"Area:{area}")
  elif type == 2: #Triangle
    print("---Area of Triangle---")
    b = int(input("base: "))
    h = int(input("height: "))
    area = 0.5 * b * h
    print(f"Area:{area}")
  elif type == 3: #Rectangle
    print("---Area of Rectangle---")
    l = int(input("length: "))
    w = int(input("width: "))
    area = l * w
    print(f"Area:{area}")
  elif type == 4: # Square
    print("---Area of Square---")
    s = int(input("what is the side: "))
    area = s ** 2
    print(f"Area:{area}")
  elif type == 5:
    print("End program. byebye!")
  else:
    print("Invalid. Please try again")

# success huhu
