from Bio import SeqIO

file1 = "C:/Users/Admin/Downloads/sequence (1).gb"
file2 = "C:/Users/Admin/Downloads/sequence (2).gb"
output_file = "combined_species.gb"

with open(output_file, "w") as outfile:

    for record in SeqIO.parse(file1, "genbank"):
        SeqIO.write(record, outfile, "genbank")


    for record in SeqIO.parse(file2, "genbank"):
        SeqIO.write(record, outfile, "genbank")

print(f"Файлы успешно объединены в {output_file}.")