
from main import Cell, Pointer


def test_integer_pointer():
    number = Cell(100)
    p = Pointer(number)

    assert p.value == 100  # Test reading

    p.value = 500

    assert number.value == 500  # Test writing


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

def test_attribute_pointer():
    class Box:
        pass

    b = Box()
    b.x = 1

    p = Pointer(b, attribute="x")
    p.value = 42

    assert b.x == 42

def test_tuple_pointer():
    data = Cell((10, 20, 30))
    p = Pointer(data, index=1)

    p.value = 99

    assert data.value == (10, 99, 30)
