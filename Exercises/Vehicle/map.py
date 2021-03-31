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

  def ReadMap(self, filePath):
    self.map = []

    if not os.path.exists(filePath):
      raise MapFileNotFoundError

    file = open(filePath, "r")

    # Luetaan tiedosto rivi kerrallaan for-silmukassa
    rowCounter = 0
    for row in file:
      row = row.strip()
      rowCounter += 1

      if self.width <= 0:
        self.width = len(row)

      mapRow = []
      # Luetaan jokainen merkki riviltä ja lisätään merkkiä vastaava maastoarvo karttaan
      for char in row:
        mapRow.append(self.GetTerrain(char))

      self.map.append(mapRow)

    self.height = rowCounter

  def GetTerrain(self, char):
    for key in values.symbols.keys():
      if values.symbols[key] == char:
        return key

    return values.Terrain.NONE
