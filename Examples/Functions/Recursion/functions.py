def rangeSum(number):
  if number == 0:  # Rekursion päättävä ehto. Löydyttävä jokaisesta rekursiivisesta funktiosta
    return 0
  return number + rangeSum(number - 1)

def rangeSum_loop(number):
  result = 0
  while number > 0:
    result += number
    number -= 1
  return result

def infinite(n=0):
  print(n)
  infinite(n + 1)

def factorial(n):
  if n < 0:
    return None
  elif n == 0 or n == 1:
    return 1

  result = 1
  while n > 1:
    result *= n
    n -= 1

  return result

def factorial_recursive(n):
  if n < 0:
    return None
  elif n == 0 or n == 1:
    return 1

  return n * factorial_recursive(n - 1)


number = 5
print("Summa:", rangeSum(number))
print("Summa:", rangeSum_loop(number))

# infinite()

print("Kertoma silmukalla", factorial(number))
print("Kertoma rekursiivisesti", factorial_recursive(number))
