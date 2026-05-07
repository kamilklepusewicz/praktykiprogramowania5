import pytest
import binary


@pytest.mark.parametrize("a, expected", [(10, "1010")])
def test_licz(a, expected):
    result = binary.licz(a, expected)
    assert result == expected


@pytest.mark.parametrize("a, expected", [(101, "Podana wartosc jest poza zakresem")])
def test_range(a, expected):
    result = binary.licz(a, expected)
    assert result == expected


@pytest.mark.parametrize(
    "a, expected", [(10.1, "Podana wartosc nie jest liczba naturalna")]
)
def test_natural(a, expected):
    result = binary.licz(a, expected)
    assert result == expected
