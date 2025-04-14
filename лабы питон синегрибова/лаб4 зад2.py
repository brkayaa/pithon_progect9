from Bio import SeqIO

def calculate_gc_content(sequence):

    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_count = len(sequence)
    if total_count == 0:
        return 0
    return (g_count + c_count) / total_count * 100

def main(input_file):
    records_gc = []

    for record in SeqIO.parse(input_file, "genbank"):
        gc_content = calculate_gc_content(str(record.seq))
        records_gc.append((record, gc_content))

    records_gc.sort(key=lambda x: x[1])

    for record, gc_content in records_gc:
        print(f"ID: {record.id}, GC Content: {gc_content:.2f}%, Sequence: {record.seq}")

if __name__ == "__main__":
    input_file ="C:/Users/Admin/PycharmProjects/PythonProject9/combined_species.gb"
    main(input_file)