#!/usr/local/bin/python3

import cgi

form = cgi.FieldStorage()
form_name = form.getvalue("submitted-name")

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
    
  </head>
  <body>
  <h1> %s </h1>
  </body>
</html> """%form_name

print(html)
