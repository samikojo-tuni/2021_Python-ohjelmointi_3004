# Harjoitus 1
# Määritä luokka Shape, josta peritään myöhemmin luokat Circle ja Rectangle.
# Shape-luokassa määritetään jäsenfunktio area, joka ylikirjoitetaan lapsiluokissa.
# Shape-luokan toteutuksessa riittää, että kyseinen funktio palauttaa arvon None
# (koska pinta-ala on mieletön käsite abstraktille kuviolle).
#
# Määritä luokka Circle, joka periytyy luokasta Shape. Circle-luokka kuvaa ympyrää
# ja sen tulisi määrittää seuraavat jäsenfunktiot:
# - area: palauttaa ympyrän pinta-alan. Ylikirjoitetaan kantaluokan toteutus
# - circumference: palauttaa ympyrän ympärysmitan.
# Mieti mitä jäsenmuuttujia luokka tarvitsee ominaisuuksien toteuttamiseksi
# ja määritä ne.

from math import pi

class Shape:
  def area(self):
    return None

class Circle(Shape):
  def __init__(self, r):
    self.r = r

  def area(self):
    return pi * self.r**2

  def circumference(self):
    return 2 * pi * self.r

# Harjoitus 2
# Määritä luokka Point. Point kuvaa pistettä 2-ulotteisessa avaruudessa.
# Mieti mitä jäsenmuuttujia kyseinen luokka tarvitsee ja toteuta ne.
#
# Määritä luokka Rectangle, joka kuvaa nelikulmiota. Rectanglen tulee periytyä
# Shape-luokasta ja se määrittellään kulmapisteiden avulla. Toteuta kulmapisteet
# määrittelmäsi Point-luokkaa käyttäen. Tässä toteutuksessa nelikulmion oletetaan
# aina olevan suorakulmio, mutta ei välttämättä neliö.
# Rectangle-luokassa toteutetaan seuraavat jäsenfunktiot:
# - area: palauttaa nelikulmion pinta-alan. Ylikirjoitetaan Shape-luokan toteutus.
# - width: palauttaa nelikulmion leveyden.
# - height: palauttaa nelikulmion korkeuden.

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Rectangle(Shape):
  def __init__(self, bottomLeft, topRight):
    self.bottomLeft = bottomLeft
    self.topRight = topRight

  def width(self):
    return self.topRight.x - self.bottomLeft.x

  def height(self):
    return self.topRight.y - self.bottomLeft.y

  def area(self):
    return self.width() * self.height()


bottomLeft = Point(0, 0)
topRight = Point(5, 10)

rectangle = Rectangle(bottomLeft, topRight)

print("Leveys", rectangle.width())
print("Korkeus", rectangle.height())
print("Pinta-ala", rectangle.area())
