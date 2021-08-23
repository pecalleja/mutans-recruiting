from collections import Counter

DNA_BASE = ["A", "T", "C", "G"]


class InvalidDna(ValueError):
    pass


def extract_dna_looking_table(dna: list[str]) -> list[str]:
    all_rows = "#".join(dna)
    traversed_dna = []
    dna_length = len(dna)
    diagonal_1, diagonal_2 = "", ""
    for i in range(dna_length):
        row = ""
        for j, element in enumerate(dna):
            if len(element) != dna_length:
                raise InvalidDna
            if element[i] not in DNA_BASE:
                raise InvalidDna
            row += element[i]
            if i == j:
                diagonal_1 += element[i]
        traversed_dna.append(row)

    for i in range(len(traversed_dna)):
        for j, element in enumerate(traversed_dna[::-1]):
            if i == j:
                diagonal_2 += element[i]

    all_columns = "#".join(traversed_dna)

    dna_looking_table = [
        all_rows, all_columns, diagonal_1, diagonal_2
    ]

    return dna_looking_table


def is_mutant(dna: list[str]):
    counter = 0
    dna_looking_table = extract_dna_looking_table(dna)
    for base in DNA_BASE:
        pattern = "".join([base] * 4)
        for dna_looking in dna_looking_table:
            counter += dna_looking.count(pattern)

    if counter > 1:
        return True
    else:
        return False
