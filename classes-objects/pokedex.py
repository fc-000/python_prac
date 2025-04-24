# pokedex exercise - fc000

class Pokemon:
  def __init__(self, name, type, level, hp, is_legendary):
    self.name = name
    self.type = type
    self.level = level
    self.hp = hp
    self.is_legendary = is_legendary

  def display_info(self):
    print(self.name)
    print(self.type)
    print(self.level)
    print(self.hp)
    print(self.is_legendary)

  def level_up(self):
    self.level = self.level + 1
    print(f"'{self.name}' is now {self.level}!")
    self.hp = self.hp + 10
    print(f"'{self.name}' now has {self.hp} hp")

  def evolve(self, new_name):
    old_name = self.name
    self.name = new_name
    print(f"'{old_name}' evolved into '{self.name}'!")

  def battle(self):
    if self.is_legendary == True:
      self.hp = self.hp - 15
      print(f"'{self.name}' did 15 hp damage")
    else:
      self.hp = self.hp - 5
      print(f"'{self.name}' did 5 hp damage")
     
articuno = Pokemon("Atricuno", "Ice", 49, 100, True)
scorbunny = Pokemon("Scorbunny", "Fire", 22, 80, False)

articuno.display_info()
articuno.level_up()
scorbunny.evolve("Raboot")
articuno.battle()
articuno.display_info()
