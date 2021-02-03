# Tuple määritellään sulkeilla
phones = ("Nokia", "Apple", "Samsung")
print(phones)

# Tuplea ei voi muuttaa sen alustuksen jälkeen. Alla oleva koodi ei toimi
# phones.append("OnePlus")
# print(phones)

# Tuplen alkioiden indeksointi:
phone = phones[1]
print(phone)

# Luo listan phones-tuplesta
phoneList = list(phones)
phoneList.append("OnePlus")
phones = tuple(phoneList)

# Tämä ei toimi. Tuple on muuttamaton tietorakenne, joten yksittäisen alkion poisto
# ei ole mahdollista edes del-komennolla
del phones[1]

# Koko tuplen pystyy poistamaan del-komennolla
del phones

print(phones)
