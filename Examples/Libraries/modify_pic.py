from PIL import Image, ImageFilter
import os

def main():
  fileName = "cat.jpg"
  picFolder = os.path.dirname(os.path.abspath(__file__))  # Karttatiedoston sisältävä kansio
  filePath = os.path.join(picFolder, fileName)

  try:
    cat = Image.open(filePath)
    cat.show()

    blurred = cat.filter(ImageFilter.BLUR)
    blurred.show()

    gray_cat = cat.convert("L")
    gray_cat.show()

    gray_cat.save(os.path.join(picFolder, "gray_cat.jpg"))
  except IOError:
    print(f"Kuvan {filePath} avaaminen ei onnistu")


if __name__ == "__main__":
  main()
