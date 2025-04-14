def calculate_gc_content(dna_sequence):
    # Считаем количество гуанина (G) в последовательности
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    # Получаем общую длину последовательности
    total_count = len(dna_sequence)

    # Если последовательность пустая, возвращаем 0
    if total_count == 0:
        return 0

    # Вычисляем процент GC-содержания
    gc_content = (g_count + c_count) / total_count * 100
    # Возвращаем процент GC-содержания
    return gc_content


def parse_fasta(file_path):
    # Создаем пустой фигню для хранения последовательностей
    sequences = {}
    # Открываем  для чтения
    with open(file_path, 'r') as file:
        identifier = None  # Инициализируем идентификатор(готовим пер, чтобы  доступна для использования в буд
       # нужно ли сохранять предыдущую последовательность.прим через иф
        sequence = []  # Инициализируем список для последовательности

        # Проходим по каждой строке файла
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Если нашли новую последовательность, сохраняем предыдущую
                if identifier is not None:
                    sequences[identifier] = ''.join(sequence)
                identifier = line[1:]
                sequence = []
            else:
                # Добавляем строку к текущей последовательности
                sequence.append(line)

        # Сохраняем последнюю последовательность, когда дошли до конца файла
        if identifier is not None:
            sequences[identifier] = ''.join(sequence)

    # Возвращаем словарь с последовательностями
    return sequences


def main(file_path):
    """Основная функция для нахождения последовательности с максимальным GC-составом."""
    # Парсим файл и получаем последовательности
    sequences = parse_fasta(file_path)
    max_gc_content = 0  # Инициализируем максимальное GC-содержание
    max_gc_id = ""  # Инициализируем идентификатор максимального GC-содержания

    # Проходим по всем последовательностям
    for identifier, dna_sequence in sequences.items():
        # Вычисляем GC-состав для текущей последовательности
        gc_content = calculate_gc_content(dna_sequence)
        # Если текущий GC-состав больше максимального, обновляем значения
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = identifier

    # Выводим идентификатор последовательности с максимальным GC-содержанием и его значение
    print(f"{max_gc_id}\n{max_gc_content:.6f}")

# Замените '1.txt' на путь к вашему файлу
main('1.txt')