Instantionate class object to read prices from YMPL webpage and write it to a csv file in structurized form.

First instantionate the object.
  example = Pricer(segments['Motocykle']['Off Road Competition'])
  segments is a dictionay with all necessary URLs.
Use Pricer' method get_roducts on an object to read parse and save prices to a file.
  example.get_products()
You can optionally print an object to display it's strucurized content in a terminal.
Finally you receive csv file in your file directory with all data.
