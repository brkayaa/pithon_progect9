#вариант 3
# Открываем файл для чтения
with open('123.txt', 'r') as file:
    lines = file.readlines()

# Предполагаем, что в файле две строки
ssss = lines[0].strip()  # первая строка
tttt = lines[1].strip()  # вторая строка

n = 0
for i in range(len(ssss)):
    if ssss[i] != tttt[i]:
        n += 1

print(n)