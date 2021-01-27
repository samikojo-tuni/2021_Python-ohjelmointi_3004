# Set määritellään aaltosulkeiden avulla {}
units = {"tank", "plane", "ship", "dog"}
print(units)

# Set ei säilytä alkioiden keskinäistä järjestystä eikä järjestykseen pidä luottaa

# Add lisää yhden alkion settiin
units.add("soldier")
print(units)

# Update lisää tietorakenteellisen (list, set, tuple) alkioita set:iin
units.update(["helicopter", "heavy tank"])
print(units)

# Discard poistaa arvon set:stä
units.discard("dog")
print(units)

units.discard("dog")
print(units)

# units.remove("dog")
# print(units)

# Discardin ja removen ero: poistaessa arvoa, jota ei löydy set:stä, remove kaataa sovelluksen,
# kun taas discard jatkaa normaalia toimintaa poistamatta mitään

# Pop poistaa "satunnaisen" arvon set:stä
units.pop()
print(units)