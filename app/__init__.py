from collections import Counter

DNA_BASE = ["A", "T", "C", "G"]


class InvalidDna(ValueError):
    pass


def extract_dna_looking_table(dna: list[str]) -> list[str]:
    all_rows = "#".join(dna)
    traversed_dna = []
    dna_length = len(dna)
    for index in range(dna_length):
        row = ""
        for element in dna:
            if len(element) != dna_length:
                raise InvalidDna
            if element[index] not in DNA_BASE:
                raise InvalidDna
            row += element[index]
        traversed_dna.append(row)
    all_columns = "#".join(traversed_dna)

    dna_looking_table = [
        all_rows, all_columns
    ]
    for element in dna_looking_table:
        print(element)
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
