# Harjoitus
# Kirjoita ohjelma, joka kysyy käyttäjän nimeä. Ohjelma tulostaa esim. tekstin
# "Mikä sinun nimesi on?"" nimeä kysyttäessä.
# Jos nimi on kirjoitettu pienellä alkukirjaimella, ohjelma muuttaa nimen alkukirjaimen
# isolla kirjoitetuksi. Lopuksi ohjelma tulostaa "Sinun nimesi on <Nimi>"

name = input("What is your name? ")

# str.capitalize() luo uuden muuttujan jonka alkukirjain on muutettu isolla
# kirjoitetuksi. Alkuperäistä muuttujaa ei muuteta. Siksi arvo pitää sijoittaa
# alkuperäiseen muuttujaan.
name = name.capitalize()

print("Your name is", name)