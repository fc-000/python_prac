co = int(input("What do you have left in pesos? "))
pe = int(input("What do you have left in soles? "))
br = int(input("What do you have left in reais? "))

co2 = co * 0.0024
pe2 = pe * 0.27
br2 = br * 0.17

total = co2 + pe2 + br2

print(total)

