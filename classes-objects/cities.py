
class Planet:
  def __init__(self, name, galaxy, distance_from_earth, moons):
    self.name = name
    self.galaxy = galaxy
    self.distance_from_earth = distance_from_earth
    self.moons = moons

planet1 = Planet("Mars", "Milky Way", 0.0000237, ["Phobos", "Deimos"])
planet2 = Planet("PA-99-N2 b", "Andromeda Galaxy", 2.5, ["none"])

print(vars(planet1))
print(vars(planet2))