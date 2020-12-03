numbers = [31, 7, 8, 23, 45, 20, 10, 15]

print("Count: ", len(numbers))
print("Max: ", max(numbers))
print("Min: ", min(numbers))
print("Sum: ", sum(numbers))

print("Average: ", sum(numbers) / len(numbers))

new_numbers = numbers[1:7]
print(new_numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

reverse_sorted_numbers = sorted(numbers, reverse=True)
print(reverse_sorted_numbers)
