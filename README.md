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
- Tuple element modification through `Cell`

### Planned

- Pointer arithmetic
- Pointer navigation (`next()` and `prev()`)
- Pointer indexing
- More supported data types

## Examples

### 1. Basic Pointer

A `Cell` allows you to create a mutable reference to a value.

```python
from main import Cell, Pointer

number = Cell(100)
p = Pointer(number)

print(p.value)  # 100

p.value = 500

print(number.value)  # 500
```

### 2. List Pointer

You can point to a specific list element using `index`.

```python
numbers = [10, 20, 30]

p = Pointer(numbers, index=1)

print(p.value)  # 20

p.value = 999

print(numbers)  # [10, 999, 30]
```

### 3. Dictionary Pointer

You can point to a dictionary value using `key`.

```python
data = {"score": 80}

p = Pointer(data, key="score")

print(p.value)  # 80

p.value = 100

print(data)  # {'score': 100}
```

### 4. Object Attribute Pointer

You can access and modify an object's attribute using `attribute`.

```python
class Box:
    pass

b = Box()
b.x = 1

p = Pointer(b, attribute="x")

print(p.value)  # 1

p.value = 42

print(b.x)  # 42
```

### 5. String Pointer

Python strings are immutable, but `Cell` allows PyPointer to replace the string after modifying a character.

```python
word = Cell("Hello")

p = Pointer(word, index=1)

p.value = "a"

print(word.value)  # Hallo
```

### 6. Tuple Pointer

Python tuples are immutable. PyPointer supports two modes of tuple access:

**Read-only mode (without `Cell`)**

You can read tuple elements through a pointer, but attempting to modify them raises a `TypeError`.

```python
data = (10, 20, 30)
p = Pointer(data, index=1)

print(p.value)  # 20

p.value = 99  # TypeError
```

**Mutable mode (with `Cell`)**

When a tuple is stored inside a `Cell`, PyPointer can modify an element by creating a new tuple and assigning it back to the `Cell`.

```python
data = Cell((10, 20, 30))
p = Pointer(data, index=1)

p.value = 99

print(data.value)  # (10, 99, 30)
```

**Explanation:** Read-only mode preserves Python's normal tuple immutability. Mutable mode uses `Cell` to provide a way to replace the tuple with an updated version.

## Error Examples

PyPointer raises exceptions when certain operations are invalid.

### 1. Accessing a Null Pointer

Trying to read or write through a null pointer raises `ReferenceError`.

```python
p = Pointer.null()

print(p.value)
# ReferenceError: Null pointer
```

### 2. Modifying a Tuple Directly

A tuple outside a `Cell` cannot be modified through a pointer.

```python
data = (10, 20, 30)

p = Pointer(data, index=1)

p.value = 99
# TypeError: 'tuple' object does not support item assignment
```

Use `Cell` if you want to modify tuple elements.

### 3. Unsupported Pointer Target

Creating a pointer to an unsupported target and trying to access its value raises `TypeError`.

```python
p = Pointer(100)

print(p.value)
# TypeError: Unsupported pointer target
```

## Project Status

PyPointer is currently a prototype under development.

Features and behavior may change as the project evolves.

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file.