#ДОП №1


def hex_output():
    """Преобразует шестнадцатеричное число в десятичное с использованием ord и chr."""
    decnum = 0
    hexnum = input('Введите шестнадцатеричное число для преобразования: ').strip()


    for power, digit in enumerate(reversed(hexnum)):
        if '0' <= digit <= '9':
            value = ord(digit) - ord('0')
        elif 'a' <= digit <= 'f':
            value = ord(digit) - ord('a') + 10
        elif 'A' <= digit <= 'F':
            value = ord(digit) - ord('A') + 10
        else:
            continue

        decnum += value * (16 ** power)

    print(decnum)
hex_output()

#ДОП №2
def name_triangle():
    """Выводит треугольник имен на основе введенного имени."""
    name = input("Введите ваше имя: ")

    for i in range(1, len(name) + 1):
        print(name[:i])

name_triangle()