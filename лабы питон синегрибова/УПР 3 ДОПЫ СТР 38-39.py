#ДОПЫ СТР 38-39
# Функция для формирования числа с плавающей точкой
def float_from_parts(number, before, after):
    """Создает число с плавающей точкой из заданных частей.

    Аргументы:
    number -- число с плавающей точкой
    before -- количество цифр до десятичной точки
    after -- количество цифр после десятичной точки

    Возвращает:
    float -- число с плавающей точкой, состоящее из частей
    """

    number_str = str(number)


    decimal_index = number_str.index('.')
    part_before = number_str[decimal_index - before: decimal_index]
    part_after = number_str[decimal_index + 1: decimal_index + 1 + after]
    result = float(f"{part_before}.{part_after}")

    return result

result = float_from_parts(1234.5678, 2, 3)
print(result)
#Использование класса Decimal для точных вычислений
from decimal import Decimal


def sum_decimals():
    """Запрашивает два числа у пользователя и выводит их сумму с использованием Decimal."""
    str1 = input("Введите первое число с плавающей точкой: ")
    str2 = input("Введите второе число с плавающей точкой: ")
    decimal1 = Decimal(str1)
    decimal2 = Decimal(str2)
    total = decimal1 + decimal2
    print(f"Сумма: {total}")
sum_decimals()