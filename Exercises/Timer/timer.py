# Kirjoita ajastin.
# Ajastin toimii siten, että käyttäjä syöttää ohjelmaan tunnit, minuutit ja sekunnit
# Tämän jälkeen ajastin lähtee laskemaan syötytystä ajasta alaspäin tulostaen uuden
# ajan sekunnin välein komentokehotteeseen.
# Ohjelman suoritus päättyy, kun ajastin käy loppuun.

# Käytä viime viikolla tekemäämme Time-luokkaa ajastimen toteuttamiseen.
# Tutustu myös Pythonin time-moduulin sleep-funktioon.

import time as t
import sys

class Time():
  def __init__(self, hours, minutes, seconds):
    # Kokonaisaika sekunteina
    self.time = hours * 3600 + minutes * 60 + seconds

  def TotalSeconds(self):
    # Jos tunnit, minuutit ja sekunnit on tallennettu omiin muuttujiinsa, pitää tässä
    # konvertoida kokonaisaika sekunneiksi
    return self.time

  def TotalMinutes(self):
    # Koska minuutissa on 60 sekuntia, saadaan kokonaisaika minuutteija jakamalla aika sekunteina 60:llä.
    return self.time // 60

  def TotalHours(self):
    return self.time // 3600

  def Hours(self):
    return self.TotalHours()

  def Minutes(self):
    # Tunnissa on 3600 sekuntia. Jakojäännöksessä on tuntiosan jälkeen jäävät sekunnit. Muutetaan ne
    # minuuteiksi jakamalla tulos 60:llä.
    return (self.time % 3600) // 60

  def Seconds(self):
    return self.time % 60

  def Decrease(self):
    self.time -= 1

  def Increase(self):
    self.time += 1

  def ToString(self):
    return f"{self.Hours():02d}:{self.Minutes():02d}:{self.Seconds():02d}"

def main():
  if len(sys.argv) == 1:
    while True:
      try:
        hours = int(input("Tunnit > "))
        minutes = int(input("Minuutit > "))
        seconds = int(input("Sekunnit > "))

        if minutes < 0 or seconds < 0 or minutes > 59 or seconds > 59:
          print("Minuuttien ja sekuntien pitää olla välillä 0-59")
          continue

        break
      except ValueError:
        print("Syötä lailliset arvot")
  elif len(sys.argv) <= 3:
    time_values = sys.argv[1].split(":")

    if len(time_values) != 3:
      print("Aika annettu väärässä formaatissa. Käytä formaattia h:m:s")
      quit()
    try:
      hours = int(time_values[0])
      minutes = int(time_values[1])
      seconds = int(time_values[2])
    except ValueError:
      print("Ajan formaatti on virheellinen")
      quit()

    message = ""
    if len(sys.argv) == 3:
      message = sys.argv[2]
  else:
    print("Virheelliset komentoriviparametrit")
    quit()

  time = Time(hours, minutes, seconds)

  while time.TotalSeconds() > 0:
    print(time.ToString())
    t.sleep(1)
    time.Decrease()

  if message != "":
    print(message)


if __name__ == "__main__":
  main()
