a = 30
b = 20

# Vertailupoeraattoreita
# == yhtäsuuruusvertailu
if a == b:
    print(a, "equals", b)
else:
    print(a, "does not equal", b)

# != erisuuruusvertailu
if a != b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

# Pythonissa erisuurruutta voidaan verrata myös not operaattorilla
if not a == b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

# < pienempi kuin, > suurempi kuin
if (a < b):  # sulkeet if-lauseessa Python-kielessä ovat valinnaiset
    print(a, "is smaller than", b)
elif a > b:
    print(a, "is greater than", b)
else:
    print(a, "equals", b)

# <= pienempi tai yhtä suuri kuin, >= suurempi tai yhtä suuri kuin
if a <= b:
    print(a, "is smaller than or equals", b)
elif a > b:
    print(a, "is greater than", b)

result = a == b
print(result)

if not result:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)
