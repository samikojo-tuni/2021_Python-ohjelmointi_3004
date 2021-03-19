from datetime import datetime

# Luokka määrittää, millaista dataa ja mitä toiminnallisuutta siitä luoduilla olioilla on.
class Contact:
  def __init__(self, first_name, last_name, phone, birth_year):
    # __init__ määrittää luokan rakentajan. Rakentaja alustaa olion alkutilaansa.
    # Rakentajaa kutsutaan automaattisesti, kun olio luodaan. Rakentaja asettaa
    # jäsenmuuttujien alkuarvot (olion alkutila)
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.birth_year = birth_year

  def ToString(self):
    # Olion jäsenmuuttujiin pääsee käsiksi self-parametrin kautta (viittaus olioon itseensä)
    # return self.first_name + " " + self.last_name + ", p. " + self.phone
    return f"{self.first_name} {self.last_name}, p. {self.phone}"

  def ToCSV(self, sep=","):
    # Serialisoidaan Contact-olio CSV-muotoon (muunnetaan muotoon joka voidaan esim. tallentaa levylle)
    return f"{self.first_name}{sep}{self.last_name}{sep}{self.phone}{sep}{self.birth_year}"

  def Age(self):
    # datetime.now() palauttaa tämänhetkisen päivämäärän ja ajan.
    # Muuttuja year palauttaa tämänhetkisen vuoden
    current_year = datetime.now().year
    age = current_year - self.birth_year
    return age
