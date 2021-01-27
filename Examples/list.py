cars = ["Toyota", "Volvo", "Mazda", "Ford"] # Hakasulkeet kuvaa listaa
print(cars)

# append lisää alkion listan loppuun
cars.append("Jeep")
print(cars)

# insert lisää alkion tiettyyn listan indeksiin
cars.insert(1, "Fiat")
print(cars)

# Poistaa alkion tietystä indeksistä
cars.pop(2)
print(cars)

# Pop ilman parametria poistaa listan viimeisen alkion
cars.pop()
print(cars)

# Remove poistaa tietyn arvon listasta
cars.remove("Toyota")
print(cars)

# Sellaisen arvon poistaminen mitä listassa ei ole kaataa sovelluksen
# cars.remove("Volvo")
# print(cars)

# Lista sallii duplikaattiarvot, tässä esimerkissä Ford on listalla kahdesti
cars.append("Ford")
print(cars)

# del-komennolla voidaan poistaa useita alkioita kerralla (indeksiväli) 
del(cars[1:3])
print(cars)

# Len palauttaa tietorakenteen pituuden
pituus = len(cars)
print(pituus)

# Funktiokutsun sisällä voidaan suorittaa toinen funktio. Sisempi suoritetaan ennen ulompaa
print(len(cars))

# Len toimii mm. myös merkkijonoille.
print(len("Tekstiä"))

# del poistaa koko listan (ja muuttujan samalla). Print(cars) kaataa tämän vuoksi skriptin
del(cars)
print(cars)
