from Bio import SeqIO

input_file = "C:/Users/Admin/PycharmProjects/PythonProject9/combined_species.gb"

for record in SeqIO.parse(input_file, "genbank"):
    print(f"Обработка записи: {record.id}")

    for feature in record.features:
        if feature.type == "CDS":

            protein_sequence = feature.qualifiers.get("translation", [""])[0]


            start = feature.location.start
            end = feature.location.end


            print(f"Белковая последовательность: {protein_sequence}")
            print(f"Кодируется участок: {record.id} от {start + 1} до {end} (1-based)")
            print()  