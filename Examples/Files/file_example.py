filePath = "Examples/Files/fruits.txt"
fruits = []

# Avataan tiedosto lukutilaan
file = open(filePath, "r")

# Käydään tiedosto läpi rivi riviltä
for row in file:
  row = row.strip()  # poistetaan white space merkit rivin alusta ja lopusta
  if row != "":  # Ei lisätä tyhjiä merkkijonoja
    fruits.append(row)

# Tiedosto on suljettava kun sitä ei enää käytetä
file.close()

for fruit in fruits:
  print(fruit)

fruits.append("Mango")
fruits.append("Kiwi")

output = ""
for fruit in fruits:
  output += fruit + "\n"

file = open(filePath, "w")  # w: ylikirjoittaa tiedoston
file.write(output)
file.close()
