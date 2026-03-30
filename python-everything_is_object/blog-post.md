# Python3: Mutable vs Immutable - Everything is an Object!

[image:0]

## Introduction

Everything in Python is an **object** with a unique **identity** (`id()`), a **type** (`type()`), and a **value**. Some objects are **mutable** (can be modified in place) like lists, others are **immutable** (cannot be changed after creation) like integers, strings, and tuples. Understanding this distinction is crucial because it affects how objects behave when assigned, passed to functions, and compared. This post explores these concepts through practical examples from my recent learning journey.

## ID and Type

Every object has a unique **identity** (memory address) accessible via `id()` and a **type** via `type()`. Small integers (-5 to 256) and the empty tuple `()` are **cached** (singletons), so multiple references point to the same object.

```python
# Integer caching
a = 89; b = 89
print(a is b)  # True (same ID)
print(id(a) == id(b))  # True

# Empty tuple singleton
a = (); b = ()
print(a is b)  # True

# Lists always different
a =; b =[1][2][3]
print(a is b)  # False (different objects)
```

**Key takeaway**: `is` checks **identity** (same object), `==` checks **value equality**.

## Mutable Objects

**Mutable objects** can be modified **in place** without creating new objects. Lists are the classic example. Methods like `append()`, `extend()`, `+=`, `pop()` modify the original object.

```python
# Same object, modified in place
l1 =[2][3][1]
l2 = l1
l1.append(4)
print(l2)  #  - l2 changed too![3][4][1][2]

# += on lists mutates in place
id_before = id(l1)
l1 +=[5]
print(id(l1) == id_before)  # True - same object
print(l1)  #[4][1][2][3][5]
```

**Crucial**: `l2 = l1` creates a **reference**, not a copy. Both point to the **same mutable object**.

## Immutable Objects

**Immutable objects** cannot be changed after creation. Modifying them creates **new objects**. Integers, strings, and tuples are immutable.

```python
# Integers: new object on modification
a = 1
id_before = id(a)
a += 1  # Creates NEW integer object
print(id(a) == id_before)  # False

# Tuples cannot be modified
t = (1, 2, 3)
# t = 99  # TypeError!

# String literals with spaces not interned
s1 = "Best School"; s2 = "Best School"
print(s1 is s2)  # False - different objects
print(s1 == s2)  # True - same value
```

**Single-element tuples** require a trailing comma: `(1,)` vs `(1)` (integer).

## Why It Matters: Python's Treatment of Mutable vs Immutable

Python treats **mutable** and **immutable** objects fundamentally differently:

| Operation | Mutable (list) | Immutable (int/tuple) |
|-----------|----------------|-----------------------|
| `l1 = l2` | Same object | Same object |
| `l1 += [4]` | Mutates in place | Creates NEW object |
| `l1.append(4)` | Mutates in place | ❌ Not possible |
| `l1 = l1 + [4]` | Creates NEW list | Creates NEW object |

```python
# += behavior difference
l1 =; id_l = id(l1)[1][2][3]
l1 +=; print(id(l1) == id_l)  # True (extend)[4]

i1 = 1; id_i = id(i1)
i1 += 1; print(id(i1) == id_i)  # False (new int)
```

**Memory optimization**: Python caches small integers and singletons (empty tuple) but creates separate tuple objects.

## Function Arguments: Pass-by-Object-Reference

Python passes **object references**, not copies. The behavior depends on **mutability**:

```python
def increment(n):
    n += 1

a = 1  # immutable
increment(a)
print(a)  # 1 - unchanged!

def append_item(lst):
    lst.append(4)

l =   # mutable[2][3][1]
append_item(l)
print(l)  #  - modified![3][1][2][4]
```

**Rebinding vs Mutation**:
```python
def rebind(lst, new_list):
    lst = new_list  # Local rebinding only!

l1 =; l2 =[6][5][1][2][3][4]
rebind(l1, l2)
print(l1)  #  - unchanged![1][2][3]
```

**To change the reference**: Return the new value:
```python
def replace_list(lst, new_list):
    return new_list.copy()

l1 = replace_list(l1, )[7][8][9]
print(l1)  #[8][9][7]
```

## Copying Mutable Objects

**Shallow copy** methods (Python 3.3+):
```python
l1 =[2][3][1]

# Three equivalent ways
l2 = l1.copy()      # Method (recommended)
l2 = l1[:]          # Slicing
l2 = list(l1)       # Constructor

l1.append(4)
print(l2)  #  - independent![3][1][2]
```

**No import needed** for `.copy()` - it's a built-in list method!

## Conclusion

Understanding **mutable vs immutable** is essential for Python mastery. **Lists** change unexpectedly through shared references, while **immutable types** are predictably safe. Use `is` for identity, `==` for equality. Always **return new values** from functions for immutables, **mutate in place** for mutables, and **copy explicitly** when needed. This knowledge prevents bugs and makes your code more predictable and efficient.

**Pro tip**: `l1 += [4]` mutates lists but rebinds integers. Know your `+=`!
