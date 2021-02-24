# Tämä scripti etsii kuvat siitä hakemistosta, missä se on ja kaikista kyseisen hakemiston
# alihakemistoista.

# Moduulin käyttöönotto. os on Pythonin sisäänrakennettu moduuli, joka sisältää järjestelmään
# liittyvää toiminnallisuutta. Import-lause ottaa moduulin käyttöön
import os

# dir: sen hakemiston tiedostopolku, mistä kuvia haetaan
# pics: lista, johon kuvien polut tallennetaan
def find_pics(dir, pics):
  # listdir palauttaa kaikki tiedostot ja hakemistot jotka ovat dir-hakemistossa
  files = os.listdir(dir)
  for file in files:
    # Tiedoston absoluuttinen polku kovalevyllä
    path = os.path.join(dir, file)
    if os.path.isdir(path):
      # Tiedosto onkin kansio, etsitään kuvia sen sisältä
      find_pics(path, pics)
    else:
      # Onko tutkittava tiedosto kuva?
      fileName = file.lower()
      if fileName.endswith(".png") or fileName.endswith(".jpg"):
        # Tiedosto on kuva
        pics.append(path)


# Lista, johon kuvat tallennetaan
pics = []
# Tämän skriptin sisältävän hakemiston polku
current_dir = os.path.dirname(os.path.realpath(__file__))
# Haetaan kuvat
find_pics(current_dir, pics)

for pic in pics:
  print(pic)
