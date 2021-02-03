counter = 10

while counter >= 0:
    print(counter)
    # Ehtoon vaikuttavan muuttujan muuttaminen silmukan sisällä on tärkeää, jotta ohjelma
    # ei jää jumiin ikuiseen silmukkaan. Ehdon täytyy siis joskus muuttua False:ksi.
    counter -= 1
    # counter = counter - 1
else:
    # Else suoritetaan, kun silmukan suoritus päättyy ilman,
    # että sitä on explisiittisesti keskeytetty
    print("Loop finished")

# break ja continue
# break keskeyttää silmukan suorituksen

counter = 10
index = 0
while counter >= 0:
    if index >= 5:
        break
    index += 1
    print(counter)
    counter -= 1
else:
    # Elseä ei suoriteta, jos silmukan suoritus keskeytettiin break:lla
    print("Loop finished")

print("\n\n")
# Tulostetaan parilliset numerot
start = 0
end = 10
while start <= end:
    start += 1
    if start % 2 != 0:  # % modulo eli jakojäännös
        continue
        # Continue hyppää silmukan seuraavalle kierrokselle
    print(start)

cars = ["Toyota", "Volvo", "Mazda", "Ford"]
for car in cars:
    print(car)

sequence = range(len(cars))
for index in sequence:
    print(index)
    # print(cars[index])

units = {"tank", "plane", "ship", "dog"}
for unit in units:
    print(unit)
