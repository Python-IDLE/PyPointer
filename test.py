
from main import Cell, Pointer


def test_integer_pointer():
    number = Cell(100)
    p = Pointer(number)

    p.value = 500

    assert number.value == 500


def test_list_pointer():
    numbers = [10, 20, 30]
    p = Pointer(numbers, index=1)

    p.value = 999

    assert numbers == [10, 999, 30]


def test_dictionary_pointer():
    data = {"score": 80}
    p = Pointer(data, key="score")

    p.value = 100

    assert data["score"] == 100


def test_string_pointer():
    word = Cell("Hello")
    p = Pointer(word, index=1)

    p.value = "a"

    assert word.value == "Hallo"


def test_null_pointer():
    p = Pointer.null()

    assert p.is_null()
