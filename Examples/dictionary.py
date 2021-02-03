# Dictionary on tietorakenne, johon tallennetaan avain-arvo -pareja

# Avaimet kannattaa tallentaa muuttujiin. Näin typojen todennäköisyys pienenee ja
# arvojen muuttaminen on helpompaa, koska muutokset pitää tehdä vain yhteen paikkaan
brandKey = "brand"
modelKey = "model"
yearKey = "year"
priceKey = "price"
colorKey = "color"

carInfo = {
    brandKey: "Toyota",
    modelKey: "Avensis",
    yearKey: 2010,
    priceKey: 8559.95
}

print(carInfo)

# Arvoja voi indeksoida avaimen perusteella
model = carInfo[modelKey]
print(model)

# Uusia avain-arvo -pareja antamalla uuden avaimen hakasulkeiden sisään ja uuden arvon
# yhtäsuuruusmerkin jälkeen
carInfo[colorKey] = "red"
print(carInfo)

carInfo[yearKey] = 2011
print(carInfo)

# Avain-arvo -pareja voidaan poistaa pop-funktiolla
price = carInfo.pop(priceKey, 0)
print(price)

# Funktio palauttaa jälkimmäisenä parametrina syötetyn oletusarvon, jos avainta ei löydy
price = carInfo.pop(priceKey, 0)
print(price)

# Virhe, jos oletusarvoa ei ole välitetty parametrina
# price = carInfo.pop("price")
# print(price)

carInfo2 = {
    brandKey: "Toyota",
    modelKey: "Avensis",
    yearKey: 2010
}

# print(carInfo, carInfo2, sep="\n")

carInfoList = [carInfo, carInfo2]
print(carInfoList)

print(carInfoList[1][yearKey])
