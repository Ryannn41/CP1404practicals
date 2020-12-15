count = {}
text = input("Text: ")

words = text.split()
print(words)
for word in words:
    frequency = count.get(word, 0)
    count[word] = frequency + 1

words = list(count.keys())
words.sort()

for word in words:
    print(word, ":", count[word])
