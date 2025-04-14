def hex_output():
    """Преобразует шестнадцатеричное число в десятичное."""
    decnum = 0
    hexnum = input('Введите шестнадцатеричное число для преобразования: ')


    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)

    print(decnum)


hex_output()
#КОРОЧЕ Я ТУТ НЕ ОСОБО ПОНЯЛА ЧТО К ЧЕМУ