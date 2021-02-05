# Harjoitus 1:
# Suunnittele ja toteuta listan väärinpäin kääntävä algoritmi. Algoritmi toimii siis siten,
# että käännetyn listan ensimmäinen alkio on alkuperäisen listan viimeinen alkio jne.
# Älä käytä list.reverse() funktiota
cars = ["Toyota", "Volvo", "Mazda", "Ford"]
reversed = []
for index in range(len(cars)):
  reversed.append(cars[-1 * (index + 1)])  # indeksointi käy listaa läpi lopusta alkuun
print(reversed)

# Harjoitus 2:
# Suunnittele ja kirjoita algoritmi, joka luo uuden sanan alkuperäisen sanan perusteella siten,
# että alkuperäisestä sanasta otetaan uuteen sanaan joka toinen kirjain.
# Ratkaisu 1:
original = "Python-ohjelmointi"
index = 0
result = ""

while index < len(original):
  # Jakojäännös, eli lasketaan index / 2, mutta ei olla kiinnostuneita tuloksesta, vaan jakojäännöksestä
  # jonka % palauttaa
  if index % 2 != 1:
    result += original[index]
  index += 1

print(result)

# Ratkaisu 2:
# Slicing & stepping
sana = "Alkuperäinen"
# Slicing:
print(sana[4:9])
# Tämä esimerkki pilkkoo alkuperäisen sanan siten, että uusi sana alkaa 5. merkistä (indeksi 4)
# ja päättyy 9. merkkiin

# Stepping
# Slicingin optionaalinen 3. parametri
# Määrittää intervallin, jonka välein merkki otetaan tulokseen mukaan
print(sana[1:10:2])
# Merkit 1-9, mutta vain joka toinen kirjain

# Täten ratkaisu voi olla seuraava:
sana = "Python-ohjelmointi"
result = sana[::2]  # Kun alkua ja loppua ei määritä, tulokseen tulee koko sana.
print(result)


# Harjoitus 3:
# Laske montako parillista ja paritonta numeroa listassa (tai tuplessa) on.
numbers = (1, 5, 2, 6, 8, 3, 4, 7, 9, 3, 4, 1)
even = 0
odd = 0
for number in numbers:
  if number % 2 == 0:
    even += 1
  else:
    odd += 1
print("Even:", even, "Odd:", odd)

# Harjoitus 4:
# Pyydä käyttäjää syöttämään sanoja, kunnes käyttäjä syöttää sanan "stop".
# Lopuksi tulosta kaikki käyttäjän syöttämät sanat (paitsi "stop").
word = ""
listOfWords = []
stopWord = "stop"

print("Syötä sanoja. Syötä sana \"stop\", kun haluat lopettaa")
while (word.lower() != stopWord):
  word = input()
  if (word.lower() != stopWord):
    listOfWords.append(word)

print(listOfWords)

# Harjoitus 5:
# Pyydä käyttäjää syöttämään, monenko luvun keskiarvon tämä haluaa laskea.
# Tämän jälkeen pyydä käyttäjää syöttämään näin monta lukua.
# Laske lopuksi lukujen keskiarvo ja tulosta tämä käyttäjälle
# num = int(input("Syötä numero "))
sum = 0.0
print("Lasketaan keskiarvo, monenko numeron keskiarvon haluat laskea?")
amount = int(input())

for num in range(amount):
  number = float(input("Syötä numero "))
  sum += number

average = sum / amount
print(average)

# Harjoitus 6
# Pyydä käyttäjää syöttämään sana. Laske montako kertaa eri kirjaimet esiintyvät sanassa.
# Lopuksi tulosta kirjaimet ja niiden esiintymiskerrat.
# Esimerkkitulosteet:
# Syötä sana > tietokone
# { "t": 2, "i": 1, "e": 2, "o": 1, "k": 1, "n": 1 }
# Vihje: operaattorit in ja not in
# Mietittäväksi: mikä tietorakenne sopii ratkaisuun?
word = input("Syötä sana ")
charCounts = {}
for char in word:
  char = char.lower()
  if char not in charCounts:
    charCounts[char] = 0
  charCounts[char] += 1

print(charCounts)
