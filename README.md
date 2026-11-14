
# PyPointer

**PyPointer** is a Python library that aims to bring C-style pointer concepts to Python.

It provides pointer-like objects that allow you to access and modify values through references to specific locations.

## Features

### Currently implemented
- Pointer objects
- Null pointers
- Read and write through `.value`
- Pointers to list elements
- Pointers to dictionary values
- Pointers to object attributes
- `Cell` objects for mutable references to immutable values
- String character access through `Cell`

### Planned
- Pointer arithmetic
- Pointer navigation (`next()` and `prev()`)
- Pointer indexing
- More supported data types

## Example

```python
from main import Cell, Pointer

# Pointer to a mutable cell
number = Cell(100)
p = Pointer(number)

print(p.value)  # 100

p.value = 500

print(number.value)  # 500
```

## List Example

```python
numbers = [10, 20, 30]

p = Pointer(numbers, index=1)

print(p.value)  # 20

p.value = 999

print(numbers)  # [10, 999, 30]
```

## Null Pointer

```python
p = Pointer.null()

print(p.is_null())  # True
```

## Project Status

PyPointer is currently a prototype under development.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file.