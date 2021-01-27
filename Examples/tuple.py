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

print(phones)