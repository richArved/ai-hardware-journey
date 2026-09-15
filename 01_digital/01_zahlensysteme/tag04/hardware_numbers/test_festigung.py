import pytest

from hardware_numbers.abschluss_tag04 import (
    to_hex,
    from_twos_complement,
    add_with_overflow_flag,
)


def test_hex_mit_null():
    assert to_hex(10, 8) == "0A"


def test_vorzeichengrenze():
    assert from_twos_complement(8, 4) == -8


def test_negativer_overflow():
    assert add_with_overflow_flag(-8, -2, 4) == (6, True)


def test_ungueltige_eingabe():
    with pytest.raises(ValueError):
        add_with_overflow_flag(8, 0, 4)