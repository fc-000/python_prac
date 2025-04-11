# April 9 2025 - Codedex Loop Recap Challenge
# Attempt 1

for i in range(1, 101):
  if i == 3: 
    i = "Fizz"
  elif i == 5:
    i = "Buzz"
  elif i == 3 * 5: #baliktad
    i = "FizzBuzz"
  print(i)


# Notes
# skeleton was kinda correct, condition was wrong

'''
Correct Code: 

for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)

via Codedex solutions
'''