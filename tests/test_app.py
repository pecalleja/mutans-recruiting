import pytest

import app.errors
from app.mutants import is_mutant


def test_basic_function():
    assert "is_mutant" in dir(app.mutants)


def test_is_mutant_return_true(dna_mutant):
    assert is_mutant(dna_mutant) is True


def test_is_mutant_return_false(dna_human):
    assert is_mutant(dna_human) is False


def test_bad_dna_count(dna_bad_count):
    with pytest.raises(app.errors.InvalidDna):
        is_mutant(dna_bad_count)


def test_bad_dna_base(dna_bad_base):
    with pytest.raises(app.errors.InvalidDna):
        is_mutant(dna_bad_base)
