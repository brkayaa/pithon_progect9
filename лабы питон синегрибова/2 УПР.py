def mysum(*numbers, start=0):
    output = start
    for number in numbers:
        output += number
    return output

# Примеры использования
print(mysum(10, 20, 30, 40))
print(mysum(1, 2, 3, start=10))
print(mysum())