from phonebook import PhoneBook
from contact import Contact
from student import Student

def main():
  phonebook = PhoneBook()

  # Kaksi oliota. Oliot on luotu samasta luokasta, mutta niillä on omat muuttujien arvonsa (olion tila)
  person1 = Contact("Maija", "Meikäläinen", "123454321", 1990)
  person2 = Contact("Matti", "Meikäläinen", "987656789", 1991)
  person3 = Student("Aimo", "Opiskelija", "1232123", 2000, 12345)

  phonebook.AddContact(person1)
  phonebook.AddContact(person2)
  phonebook.AddContact(person3)

  phonebook.PrintContacts()

  # print(person1.ToString())
  # print(person2.ToString())

  # print("Person 1's age:", person1.Age())


if __name__ == "__main__":
  main()
