import values
import os

class MapFileNotFoundError(FileNotFoundError):
  pass

class Map():
  def __init__(self, mapFilePath):
    self.width = 0  # Kartan leveys
    self.height = 0  # Kartan korkeus

    # Luetaan kartta tiedostosta
    self.ReadMap(mapFilePath)

  def Draw(self, *vehicles):
    print("  ", end="")

    for column in range(1, self.width + 1):
      print(column % 10, end="")  # % modulo eli jakojäännösoperaattori

    print()  # Tulostetaan pelkkä rivinvaihto

    for row in range(self.height):
      print(str(row + 1), end=" ")

      for column in range(self.width):
        # Selvitetään tutkittavassa koordinaatissa oleva Terrain-tyyppi
        terrain = self.GetTerrainAt(column, row)
        # Haetaan Terrain-tyyppiä vastaava symboli, joka piirretään
        symbol = self.GetSymbol(terrain)

        for vehicle in vehicles:
          if vehicle.position[0] == column and vehicle.position[1] == row:
            # Ajoneuvo on tässä koordinaatissa, piirretään sitä vastaava symboli
            symbol = vehicle.GetSymbol()
            break  # Oikea ajoneuvo löytyi, poistutaan silmukasta (mikro-optimointi)

        print(symbol, end="")

      print()  # Rivinvaihto

  def ReadMap(self, filePath):
    self.map = []

    if not os.path.exists(filePath):
      raise MapFileNotFoundError

    file = open(filePath, "r")

    # Luetaan tiedosto rivi kerrallaan for-silmukassa
    for row in file:
      row = row.strip()  # Poistaa white spacet rivin alusta ja lopusta

      if self.width <= 0:
        self.width = len(row)

      mapRow = []
      # Luetaan jokainen merkki riviltä ja lisätään merkkiä vastaava maastoarvo karttaan
      for char in row:
        mapRow.append(self.GetTerrain(char))

      self.map.append(mapRow)

    self.height = len(self.map)

    file.close()

  def GetTerrain(self, char):
    for key in values.symbols.keys():
      if values.symbols[key] == char:
        return key

    return values.Terrain.NONE

  def GetTerrainAt(self, column, row):
    if column < 0 or row < 0 or column >= self.width or row >= self.height:
      # Koordinaatti kartan ulkopuolella
      raise IndexError

    return self.map[row][column]  # Arvon palauttaminen 2 ulotteisesta listasta

  def GetSymbol(self, terrain: values.Terrain):
    if terrain in values.symbols:
      return values.symbols[terrain]

    raise IndexError
