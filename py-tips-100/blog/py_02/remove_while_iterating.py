numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)

numbers = [1, 2, 3, 4, 5, 6]
numbers = [number for number in numbers if number % 2 != 0]
print(numbers)
