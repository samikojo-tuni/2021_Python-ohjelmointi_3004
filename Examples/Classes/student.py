from contact import Contact

# Student periytyy Contact-luokasta. Ts. Student on Contact-luokan lapsi
class Student(Contact):
  def __init__(self, first_name, last_name, phone, birth_year, student_number):
    # Contact-luokan rakentajan kutsu. super() palauttaa viittauksen kantaluokkaan.
    super().__init__(first_name, last_name, phone, birth_year)
    self.student_number = student_number

  # Jos funktio on jo määritetty kantaluokassa, funktion määrittäminen uudelleen lapsiluokassa
  # ylikirjoittaa kantaluokan toteutuksen
  def ToString(self):
    base = super().ToString()  # Kantaluokan toteutuksen suoritus
    return f"{base} #{self.student_number}"
