# attempt with some Codedex solution implementation

warriors = [
          {"name":"Stephen Curry", "number": "30", "position":"point guard", "three-point-percentage": 42.3,},
          {"name":"Jimmy Butler", "number": "10", "position":"Small forward", "three-point-percentage": 32.8,},
          {"name":"Draymond Green", "number": "23", "position":"power forward", "three-point-percentage": 32.0}
]

names = [player["name"] for player in warriors]
print("Players Names:", names)

warriors[0]["three-point-percentage"] = 43.0

total_tpp = 0
for player in warriors:
    total_tpp += player['three-point-percentage']

average = total_tpp / len(warriors)
print("Average three-point-percentage:", average)