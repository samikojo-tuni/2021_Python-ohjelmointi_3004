import json

def main():
  data = []

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

  carInfo2 = {
    brandKey: "Toyota",
    modelKey: "Avensis",
    yearKey: 2010,
    priceKey: 8000
  }

  data.append(carInfo)
  data.append(carInfo2)

  jsonText = json.dumps(data, indent=2)

  print(jsonText)

  file = open("cars.json", "w", encoding="utf-8")
  file.write(jsonText)
  file.close()


if __name__ == "__main__":
  main()
