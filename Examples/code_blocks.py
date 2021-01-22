num1 = 2
num2 = 2

# Ehtolause: jos lause on tosi, suoritetaan siihen liittyvä koodiblokki,
# muussa tapauksessa tehdään jotain muuta

# Koodiblokki tulktaan sisennysten perusteella. Esim. if-ehtolausetta vastaava
# blokki pitää sisentää, jotta Python osaa tulkita sen kuuluvaksi if-ehtolauseeseen
if num1 > num2:
    print("num1 on suurempi")
elif num2 > num1:
    print("num2 on suurempi")
else:
    print("numerot ovat yhtä suuret")
    print("anna jotkin muut numerot")

print("Ohjelma päättyy")