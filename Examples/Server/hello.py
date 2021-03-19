#!/usr/bin/python3

import cgi
import cgitb
import os

# Virheenkäsittelijä, joka osaa tulostaa tietoa skriptissä olevasta virheestä
cgitb.enable()

print("Content-type: text/html\n")

def get_page_content(page_number):
  if page_number == 1:
    return "<p>Sivu 1</p>"
  elif page_number == 2:
    return "<p>Sivu 2</p>"
  else:
    return "<p>Tuntematon sivu</p>"


# Selvitetään kutsussa käytetty HTTP-metodi
http_method = os.environ["REQUEST_METHOD"]

data = cgi.FieldStorage()
page_number = int(data.getvalue("page", 1))

page = f''' 
<html>
<head><title>Testisivu</title></head>
<body>
<h1>Testisivu</h1>
<p>Http-metodi: {http_method}</p>
{get_page_content(page_number)}
<p>page_number: {page_number}</p>
</body>
</html>
'''

print(page)
