from palmerpenguins import load_penguins

from app import filter_penguins


def test_filter_penguins():
    penguins = load_penguins()
    calculated = filter_penguins(["Adelie"])
    expected = penguins[penguins.species.isin(["Adelie"])]

    print(calculated.head())
    print(expected.head())

    assert calculated.equals(expected)
