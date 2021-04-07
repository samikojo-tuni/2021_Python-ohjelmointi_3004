from values import Terrain, Direction
from map import Map

class Vehicle:
  ''' Kantaluokka kaikille ajoneuvoille '''

  def __init__(self, speed, x, y):
    ''' Määrittää ajoneuvon ominaisuudet.

        Parametrit:
        speed: ajoneuvon nopeus peliruutuina / vuoro
        x: ajoneuvon x-koodrinaatti kartalla
        y: ajoneuvon y-koordinaatti kartalla
    '''
    self.speed = speed
    self.position = (x, y)
    self.InitAllowedTerrains()

  def InitAllowedTerrains(self):
    ''' Määrittää millaisessa maastossa ajoneuvolla voi ajaa. Arvot values.Terrain-enumin arvoja.
    '''
    self.allowedTerrains = [Terrain.NONE]

  def GetName(self):
    ''' Palauttaa ajoneuvon nimen. '''
    return ""

  def GetSymbol(self):
    ''' Palauttaa symbolin, jolla ajoneuvo piirretään karttaan. '''
    return " "

  def Move(self, direction: Direction, map: Map):
    ''' Liikuttaa ajoneuvoa haluttuun suuntaan.

        Kohdekoordinaatti riippuu ajoneuvon nopeudesta. Osa ajoneuvoista voi liikkua vain tietynlaisessa 
        maastossa. Varmista, että ajoneuvo ei liiku sellaiseen maastoon, jossa se ei voi kulkea.
        Ajoneuvo liikkuu sen nopeuden määrittämän määrän ruutuja vuoron aikana suuntaan direction, mutta
        kuitenkin siten, että se ei päädy koskaan sellaiselle maastolle, missä se ei voi kulkea.
        Esimerkiksi jos ajoneuvon nopeus on kaksi, mutta kulkusuunnassa on vain yksi ruutu maastoa, jossa
        ajoneuvo voi kulkea, liikkuu ajoneuvo vain yhden ruudun.
        Metodi asettaa self.position muuttujan arvon siihen koordinaattiin, johon ajoneuvo on
        liikkunut.
    '''
    pass

class Car(Vehicle):
  def __init__(self, x, y):
    super().__init__(2, x, y)
    self.name = "Auto"
    self.symbol = "A"

  def InitAllowedTerrains(self):
    self.allowedTerrains = [Terrain.GROUND]

  def GetName(self):
    return self.name

  def GetSymbol(self):
    return self.symbol

class Plane(Vehicle):
  def __init__(self, x, y):
    super().__init__(3, x, y)

  def InitAllowedTerrains(self):
    self.allowedTerrains = [Terrain.GROUND, Terrain.WATER]

  def GetName(self):
    return "Lentokone"

  def GetSymbol(self):
    return "L"

class Boat(Vehicle):
  def __init__(self, x, y):
    super().__init__(1, x, y)
    self.name = "Vene"
    self.symbol = "V"

  def InitAllowedTerrains(self):
    self.allowedTerrains = [Terrain.WATER]

  def GetName(self):
    return self.name

  def GetSymbol(self):
    return self.symbol
