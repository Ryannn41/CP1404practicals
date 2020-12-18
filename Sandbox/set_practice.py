"""create set"""

s = {2, 3, 4, 5, 5, 5, 6, 7, 7, 8}  # element in set can not be repeated
print(s)

"""set()"""

sl = set(range(6))
print(sl, type(sl))

"""set add/delete/clear"""
s = {10, 20, 30, 405, 60}
'''bool'''
print(10 in s)  # Ture
print(999 in s)  # False

'''add element in set'''
s.add(80)  # add one element use add
print(s)
s.update({200, 400, 300})  # add at least one element use update
print(s)
s.update([100, 88, 8])
s.update((78, 64, 56))
print(s)

'''delete elment in set'''
s.remove(100)
print(s)
# s.remove(500)  # KeyError: 500
# print(s)

s.discard(500)
print(s)  # use discard no Keyerror

s.pop()  # pop randomly delete one element
print(s)
s.pop()
print(s)
s.clear()  # clear all elements of set
print(s)
