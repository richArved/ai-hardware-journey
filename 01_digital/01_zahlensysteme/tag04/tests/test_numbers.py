"""Spezifikationstests: zu Beginn absichtlich rot, bis du implementiert hast."""
import pytest

from hardware_numbers.numbers import (
    to_bin, to_hex, from_twos_complement, add_with_overflow_flag,
)


@pytest.mark.parametrize("value,bits,expected", [
    (0, 1, "0"), (1, 1, "1"), (0, 8, "00000000"),
    (5, 8, "00000101"), (255, 8, "11111111"),
    (17, 5, "10001"), (1 << 64, 65, "1" + "0" * 64),
])
def test_to_bin(value, bits, expected):
    assert to_bin(value, bits) == expected


@pytest.mark.parametrize("value,bits,expected", [
    (0, 8, "00"), (10, 8, "0A"), (255, 8, "FF"),
    (1, 1, "1"), (31, 5, "1F"), (2748, 12, "ABC"),
    (1 << 64, 65, "1" + "0" * 16),
])
def test_to_hex(value, bits, expected):
    assert to_hex(value, bits) == expected


@pytest.mark.parametrize("raw,bits,expected", [
    (0, 8, 0), (127, 8, 127), (128, 8, -128), (255, 8, -1),
    (0, 1, 0), (1, 1, -1), (16, 5, -16), (15, 5, 15),
    (1 << 64, 65, -(1 << 64)),
])
def test_from_twos_complement(raw, bits, expected):
    assert from_twos_complement(raw, bits) == expected


@pytest.mark.parametrize("a,b,bits,expected", [
    (0, 0, 8, (0, False)), (12, 30, 8, (42, False)),
    (127, 0, 8, (127, False)), (-128, 0, 8, (-128, False)),
    (127, 1, 8, (-128, True)), (-128, -1, 8, (127, True)),
    (-1, 1, 8, (0, False)), (-128, 127, 8, (-1, False)),
    (-1, -1, 8, (-2, False)), (64, 64, 8, (-128, True)),
    (-128, -128, 8, (0, True)), (-1, -1, 1, (0, True)),
    (15, 1, 5, (-16, True)),
    ((1 << 64) - 1, 1, 65, (-(1 << 64), True)),
])
def test_add_with_overflow_flag(a, b, bits, expected):
    result = add_with_overflow_flag(a, b, bits)
    assert result == expected
    assert type(result[1]) is bool


@pytest.mark.parametrize("function", [to_bin, to_hex, from_twos_complement])
@pytest.mark.parametrize("value,bits", [(0, 0), (0, -1), (-1, 8), (256, 8), (32, 5)])
def test_invalid_unsigned_input(function, value, bits):
    with pytest.raises(ValueError):
        function(value, bits)


@pytest.mark.parametrize("a,b,bits", [
    (0, 0, 0), (0, 0, -1), (128, 0, 8), (0, 128, 8),
    (-129, 0, 8), (0, -129, 8), (1, 0, 1),
])
def test_invalid_add_input(a, b, bits):
    with pytest.raises(ValueError):
        add_with_overflow_flag(a, b, bits)
