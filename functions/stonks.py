# Stonks 📈
# Codédex

'''

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
  return stock_prices[i-1]

def max_price(a, b):
  mx = 0
  for i in range(a, b + 1):
    mx = max(mx, price_at(i))
    print(mx)

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b + 1):
    mn = min(mn, price_at(i))
    print(mn)

print(max_price(1, 15))
print(min_price(5, 10))
print(price_at(3))

'''

temperatures = [22.0, 21.0, 30.0, 24.0, 40.0, 
                43.0, 35.0, 23.0, 10.0, 20.0, 
                23.0, 25.0, 33.0, 31.0, 35.0,
                39.0, 41.0, 49.0, 48.00, 45.0,
                44.0, 50.0, 52.0, 58.0, 55.0,
                27.0, 32.0, 36.0, 37.0, 38.0]

def temp_on(i):
  return temperatures[i-1]

def max_temp(a, b):
  mx = 0
  for i in range (a, b + 1):
    mx = max(mx, temp_on(i))
  return mx
def min_temp(a, b):
  mn = temp_on(a)
  for i in range (a, b + 1):
    mn = min(mn, temp_on(i))
  return mn
  

print(max_temp(5, 15))
print(min_temp(20, 30))  
print(temp_on(10))

'''
notes/mistake:

place return outside of the loop to print only single values

'''