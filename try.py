import datetime
somethingx = '02-03-2023'
print(str(datetime.datetime.strptime(str(somethingx), "%d-%m-%Y").strftime("%B %d, %Y")))
