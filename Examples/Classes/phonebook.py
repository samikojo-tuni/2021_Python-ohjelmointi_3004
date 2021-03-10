from contact import Contact

class PhoneBook:
  def __init__(self):
    self.contacts = []

  def AddContact(self, person: Contact):
    self.contacts.append(person)

  def PrintContacts(self):
    for person in self.contacts:
      print(person.ToString())
