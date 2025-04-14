
#СТР  33-34 ВРОДЕ ДОПЫ


def mysum(*numbers, start=0):
    total = start
    for number in numbers:
        total += number
    return total

print(mysum(10, 20, 30, 40))
print(mysum(1, 2, 3, start=10))
print(mysum())
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


print(average([1, 2, 3, 4, 5]))
print(average([]))

def word_lengths(words):
    if not words:
        return (0, 0, 0)

    lengths = [len(word) for word in words]
    return (min(lengths), max(lengths), sum(lengths) // len(lengths))


print(word_lengths(["apple", "banana", "kiwi"]))

def sum_numbers(objects):
    total = 0
    for obj in objects:
        try:
            total += int(obj)
        except (ValueError, TypeError):
            continue
    return total


print(sum_numbers([1, '2', 3.5, 'four', 5]))
print(sum_numbers(['10', '20', 'invalid', 30]))


