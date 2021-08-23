import app
import pytest


def test_basic_function():
    assert "is_mutant" in dir(app)


def test_is_mutant_return_true(dna_mutant):
    assert app.is_mutant(dna_mutant) is True


def test_is_mutant_return_false(dna_human):
    assert app.is_mutant(dna_human) is False


def test_bad_dna_count(dna_bad_count):
    with pytest.raises(app.InvalidDna):
        app.is_mutant(dna_bad_count)


def test_bad_dna_base(dna_bad_base):
    with pytest.raises(app.InvalidDna):
        app.is_mutant(dna_bad_base)
