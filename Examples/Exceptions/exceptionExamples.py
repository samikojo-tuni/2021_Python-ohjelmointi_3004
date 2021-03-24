def main():
  # Käyttäjä syöttää kaksi lukua. Luvuilla suoritetaan jakolasku.
  jatka = True
  while jatka:
    try:
      print("Jakolasku")
      jaettava = int(input("Jaettava "))
      jakaja = int(input("Jakaja "))

      tulos = jaettava / jakaja
      print(f"Tulos {tulos}")

      jatka = False

    except TypeError:
      print("Tekstillä ei voida suorittaa laskutoimituksia")
    except ValueError:
      print("Syötä vain numeroita!")
    except ZeroDivisionError:
      print("Nollalla jakaminen ei ole sallittua!")
    except KeyboardInterrupt:
      raise Exception()
    except:
      print("Tuntematon virhe")


if __name__ == "__main__":
  main()
