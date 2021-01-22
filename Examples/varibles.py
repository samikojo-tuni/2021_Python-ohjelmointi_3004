# Muuttujalle ei määritellä tyyppiä, Python osaa tulkita sen arvosta
muuttuja1 = 1 # Integer, kokonaisluku
muuttuja2 = "tekstiä" # string, merkkijono

# Dynaamisesti tyypitetty kieli, muuttujan uudelleenmääritys voi muuttaa myös tyypin
muuttuja1 = "Tekstiä" # Muuttuja oli aiemmin integer-tyyppinen, nyt string

# Tyyppejä
muuttuja1 = 1 # Integer, kokonaisluku
muuttuja2 = "tekstiä" # string, merkkijono
muuttuja3 = 1.2 # Float, desimaaliluku
muuttuja4 = True # Boolean, totuusarvo: True tai False

numero1 = 2
numero2 = 4

tulos = 0

# Yhteenlasku
tulos = numero1 + numero2
print(tulos)

# Vähennetään tuloksesta numero1
# tulos = tulos - numero1, sama kuin alla oleva
tulos -= numero1
print(tulos)

# Vastaavasti: 
# += Lisäys ja sijoitus
# -= vähennys ja sijoitus
# *= kertolasku ja sijoitus
# /= jakolasku ja sijoitus, tulos desimaaliluku
# //= jakolasku ja sijoitus, tulos kokonaisluku

tulos = numero1 * numero2
print(tulos)

# Tämä eroaa Javasta ja vastaavista kielistä, kahden integerin välinen jakolasku
# palauttaa floating point -arvon
tulos = numero1 / numero2
print(tulos)

# Jos jakolaskun halutaan palauttavan integerin, pitää jakomerkkejä kirjoittaa kaksi
# kappaletta //
tulos = numero1 // numero2
print(tulos)

muuttuja1 = 10
muuttuja2 = "Testi"
# Pythonissa eri tyyppisiä muuttujia ei voi yhdistää yhteenlaskulla
# Muuttujille on ensin tehtävä tyyppimuunnos
# Esim. str(muuttuja1) muuttaa muuttuja1 arvon 10 (integer) arvoksi "10" (string)
# C#-kielessä lopputulos olisi ollut "Testi10"
# Python on vahvasti tyypitetty kieli, eri tyyppisiä muuttujia ei voi esim. laskea
# yhteen

# Ulos kommentoitu koodirivi. Tulkitaan kommentiksi, joten sitä ei suoriteta
# print(muuttuja2 + muuttuja1)

# Koska yllä oleva rivi oli virheellinen, tätä riviä ei enää suoriteta
print("Tulostuuko tämä?")
print('Tämä on vastaavasti merkkijono')
print('Tulostetaan "lainaus"') # Lainausmerkkien käyttö merkkijonon sisällä
print("Tulostetaan \"lainaus\"") # Lainausmerkit voidaan merkitä kenoviivalla, jolloin
# se tulkitaan kuuluvan osaksi merkkijonoa

# Jos haluamme jatkaa koodiriviä toiselle riville, meidän on käytettävä rivinvaihto-
# merkkiä \
print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod \
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, \
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo \
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse \
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non \
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

# """ voidaan käyttää usean rivin merkkijonojen määrittämiseen
longText = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(longText)

# """ voi käyttää myös usean rivin mittaisena kommenttina,
# jos sitä ei sijoita muuttujaan
""" Usean
rivin 
kommentti
"""

# Vastaavasti
# int(muuttuja) muuttaa muuttujan integeriksi
# float(muuttuja) muuttaa muuttujan desimaaliluvuksi
# str(muuttuja) muuttaa muuttujan stringiksi

# Boolean eli totuusarvo
# Arvo 0 (int, float) vastaa totuusarvoa False, mikä tahansa nollasta poikkeava
# vastaa totuusarvoa True