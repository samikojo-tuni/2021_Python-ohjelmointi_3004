PI = 3.14159265359

def max(*numbers):
  maxValue = None
  for number in numbers:
    if maxValue == None or number > maxValue:
      maxValue = number
  return maxValue


def min(*numbers):
  minValue = None
  for number in numbers:
    if minValue == None or number < minValue:
      minValue = number
  return minValue

def average(numbers: list):
  result = 0

  for number in numbers:
    result += number

  length = len(numbers)
  average = result / length

  return average

def factorial(n):
  if n < 0:
    return None
  elif n == 0 or n == 1:
    return 1

  return n * factorial(n - 1)

def main():
  numbers = [1, 2, 3, 4, 5]
  avg = average(numbers)
  print("Keskiarvo", avg)


if __name__ == "__main__":
  main()
