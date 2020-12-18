"""use zip() to create dict"""

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
lst = zip(items, prices)
print(list(lst))

dict = {item: price for item, price in zip(items, prices)}
print(dict)
