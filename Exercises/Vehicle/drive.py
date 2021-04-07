''' Tässä moduulissa toteutetaan pelin pääohjelma. '''
from os import name, system, path
from vehicle import Vehicle, Car, Boat, Plane
import values
from map import Map, MapFileNotFoundError

def clear():
  '''
  Tyhjentää komentokehotteen. Tukee Windows ja Linux/macOS järjestelmiä.
  '''
  if name == "nt":
    # Windows
    system("cls")
  else:
    # Jokin muu (Linux/macOS)
    system("clear")

def main():
  # TODO: Lue kartan sijainti komentoriviparametrina
  mapFolder = path.dirname(path.abspath(__file__))  # Karttatiedoston sisältävä kansio
  mapFile = path.join(mapFolder, values.default_map)  # Karttatiedoston polku kiintolevystä

  try:
    map = Map(mapFile)
  except MapFileNotFoundError:
    print("Karttatiedostoa ei löytynyt!")
    return  # Return tässä sulkee sovelluksen

  car = Car(1, 1)
  plane = Plane(3, 3)
  boat = Boat(7, 3)

  currentVehicle = car  # Liikutetaan autoa oletuksena

  command = ''
  while command != 'q':
    clear()

    map.Draw(car, plane, boat)

    print("Valittu ajoneuvo", currentVehicle.GetName())

    command = input("Syötä komento: > ").strip().lower()
    if command == "up":
      currentVehicle.Move(values.Direction.UP, map)
    elif command == "down":
      currentVehicle.Move(values.Direction.DOWN, map)
    elif command == "left":
      currentVehicle.Move(values.Direction.LEFT, map)
    elif command == "right":
      currentVehicle.Move(values.Direction.RIGHT, map)
    elif command == "p":
      currentVehicle = plane
    elif command == "c":
      currentVehicle = car
    elif command == "b":
      currentVehicle = boat


if __name__ == "__main__":
  main()
