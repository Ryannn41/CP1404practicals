""" Get dict element """

scores = {'Alice': 100, 'Ryan': 98, 'David': 45}
"""method 1: use []"""
print(scores['Alice'])
# print(scores['Sam'])  # KeyError: 'Sam'


"""method 2: use get()"""
print(scores.get('Alice'))
print(scores.get('Sam'))  # None

"""key bool"""
print('Alice' in scores)
print('Alice' not in scores)

"""delete/add/clear element"""
del scores['Alice']  # delete specified element
print(scores)

scores.clear()  # delete all
print(scores)

scores['Sam'] = 60  # add element
print(scores)

"""get key"""
scores = {'Alice': 100, 'Ryan': 98, 'David': 45}
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # convert dict_key to list

"""get value"""
values = scores.values()
print(values)
print(type(values))
print(list(values))  # convert dict_value to list

"""get all key-value"""
items = scores.items()
print(items)
print(type(items))
print(list(items))  # convert key-value to list
