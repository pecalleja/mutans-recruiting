import pytest


@pytest.fixture()
def dna_mutant():
    return [
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG"
    ]


@pytest.fixture()
def dna_human():
    return [
        "TTGCCA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG"
    ]


@pytest.fixture()
def dna_bad_base():
    return [
        "ETGCCA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG"
    ]


@pytest.fixture()
def dna_bad_count():
    return [
        "TTGCCA",
        "CAGTGC",
        "TTATGT",
        "AGAAG",
        "CCCCTA",
        "TCACTG"
    ]
