"""View all element in dict"""

scores = {'Alice': 100, 'Ryan': 98, 'David': 45}
for item in scores:
    print(item, scores.get(item))

"""Feature test of dict"""

d = {'name': 'Alice', 'name': 'Sam'}  # key can not be repeated
print(d)

d = {'name': 'Alice', 'nickname': 'Alice'}  # value can be repeated
print(d)


"""Dict is unordered (hash)"""
list = [10, 20, 30]
list.insert(1, 100)
print(list)
# d = {list:100}  # TypeError: unhashable type: 'list'
print(d)

#  dict waste major memory, converting space for time
