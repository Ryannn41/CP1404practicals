from operator import itemgetter

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]

# Gives [['Bob', 6], ['Derek', 7], ['Carrie', 8], ['Aaron', 9]]
data.sort(key=itemgetter(1))
print(data)

# Sort by 2nd then 1st elements
data.sort(key=itemgetter(1, 0))
