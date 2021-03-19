from contact import Contact
from os import path

class PhoneBook:
  def __init__(self, filePath, sep):
    self.contacts = []
    self.file_path = filePath
    self.ReadContacts(sep)

  def ReadContacts(self, sep=","):
    # Tarkistetaan, onko tiedosto olemassa
    if path.exists(self.file_path):
      # Tiedosto löytyy, luetaan se
      file = open(self.file_path, "r", encoding="utf-8")
      for row in file:
        contact = row.strip().split(sep)

        contact_obj = Contact(contact[0], contact[1], contact[2], contact[3])
        self.contacts.append(contact_obj)

      file.close()

  def SaveContacts(self, sep=","):
    output = ""
    for contact in self.contacts:
      output += contact.ToCSV(sep) + "\n"

    file = open(self.file_path, "w", encoding="utf-8")
    file.write(output)
    file.close()

  def AddContact(self, person: Contact):
    self.contacts.append(person)

  def PrintContacts(self):
    for person in self.contacts:
      print(person.ToString())
