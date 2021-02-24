# Funktio määritetään def-avainsanalla. Funktio input (parametrit) määritetään sulkeiden sisällä
# Muuttujan tyypin voi määrittää parametrille, mutta tulkki ei määrityksestä välitä, vaan
# päättelee tyypin ajon aikana. Tyyppimääritys on vain vihje ohjelmoijalle
isAverageRun = False

# Pythonissa voimme määrittää vain yhden tietyn nimisen funktion. Funktioiden overloadaus
# ei ole mahdollista.
# parametrille voidaan määrittää oletusarvo, esim. printResult=True. Oletusarvo toimii siten,
# että mikäli funktiota kutsuttaessa parametrille ei anneta arvoa, saa se arvokseen oletusarvon
def average(numbers: list, printResult: bool = True):
  result = 0

  # global avainsanan avulla voimme muuttaa globaalin muuttujan arvoa funktion sisällä
  global isAverageRun

  for number in numbers:
    result += number

  # Funktio voi myös kutsua muita funktioita oman toiminnallisuutensa toteuttamiseksi
  # (kuten len-funktiota tässä esimerkissä)
  length = len(numbers)
  average = result / length

  if printResult:
    print(average)

  # Funktio muuttaa ohjelman tilaa, sillä on siis ns. sivuvaikutuksia
  isAverageRun = True
  print(isAverageRun)

  return average


avg = average([1, 2, 3, 4, 5])

# Summan laskeva funktio. Ottaa vastaan määrittämättömän määrän paramerteja.
def sum(*numbers):
  result = 0
  for number in numbers:
    if result == 0:
      index = 0
    else:
      index += 1
    result += number

  # index:n arvo voidaan lukea tässä, vaikka se on määritetty for-silmukan sisällä. Funktion
  # ulkopuolella sen arvoa ei kuitenkaan enää voida lukea.
  # Jos muuttujaa ei ole tässä vaiheessa koskaan asetettu (tässä esimerkissä jos funktio saa
  # inputtina nolla parametria), index:n luku tässä kohdassa aiheuttaa virheen (alustamatonta
  # muuttujaa ei voida lukea)
  if len(numbers) > 0:
    print("Index:", index)

  return result


def main():
  numbers = [1, 2, 3, 4, 5]

  avg = average(numbers)
  print(isAverageRun)

  numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
  print(average(numbers, False))

  summa = sum(1, 2, 3, 4, 5, 6, 7, 8)
  summa2 = sum()
  print(summa)
  print(summa2)


# Tapa toteuttaa main-funktio Pythonissa. Määritetään kaikki muu koodi paitsi alla oleva ja
# globaalit muuttujat funktioiden sisällä.
if __name__ == "__main__":
  main()
