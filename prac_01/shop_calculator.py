total_price = 0
num_items = int(input('Number of items: '))
for i in range(num_items):
    price_items = float(input('Price of items: '))
    total_price += price_items

if total_price > 100:
    total_price = total_price * 0.9
print('Total price for ', num_items, ' items is $', total_price, sep='')
