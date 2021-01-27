# Dictionary on tietorakenne, johon tallennetaan avain-arvo -pareja
carInfo = {
	"brand": "Toyota",
	"model": "Avensis",
	"year": 2010,
	"price": 8559.95
}

print(carInfo)

# Arvoja voi indeksoida avaimen perusteella
model = carInfo["model"]
print(model)

# Uusia avain-arvo -pareja antamalla uuden avaimen hakasulkeiden sisään ja uuden arvon 
# yhtäsuuruusmerkin jälkeen
carInfo["color"] = "red"
print(carInfo)

carInfo["year"] = 2011
print(carInfo)

# Avain-arvo -pareja voidaan poistaa pop-funktiolla
price = carInfo.pop("price", 0)
print(price)

# Funktio palauttaa jälkimmäisenä parametrina syötetyn oletusarvon, jos avainta ei löydy
price = carInfo.pop("price", 0)
print(price)

# Virhe, jos oletusarvoa ei ole välitetty parametrina
# price = carInfo.pop("price")
# print(price)

carInfo2 = {
	"brand": "Toyota",
	"model": "Avensis",
	"year": 2010
}

# print(carInfo, carInfo2, sep="\n")

carInfoList = [carInfo, carInfo2]
print(carInfoList)

print(carInfoList[1]["year"])
