# Python PEP 8 Style Guide for Data Science & AI

PEP 8 defines conventions to make Python code readable and consistent. Adhering to these guidelines helps teams collaborate and maintain code easily. The following sections summarize essential rules with examples of correct and incorrect usage.

## Naming Conventions

### Function and Variable Names
Use snake_case (lowercase with underscores).

```python
# Correct:
def load_data(file_path):
    pass

# Wrong:
def LoadData(filepath):
    pass
```

### Class Names
Use CapWords (PascalCase).

```python
# Correct:
class DataProcessor:
    pass

# Wrong:
class data_processor:
    pass
```

### Constants
Use ALL_CAPS with underscores.

```python
# Correct:
MAX_EPOCHS = 10

# Wrong:
maxEpochs = 10
```

### Module Names
Use short, lowercase names (underscores allowed for readability) (e.g. `data_utils.py`).

### Internal Names
Prefix a single underscore for non-public variables or methods (e.g. `_helper`). For argument names that clash with Python keywords, append a single underscore (e.g. `class_`).

## Code Layout and Indentation

### Indentation
Use 4 spaces per indentation level; never mix tabs and spaces.

```python
# Correct:
for item in data:
    process(item)

# Wrong (2-space indent):
for item in data:
  process(item)
```

### Blank Lines
Use blank lines to separate sections of code. Surround top-level class and def definitions with two blank lines (see Function and Class Definitions below).

## Imports

### One per Line
Place each import on its own line.

```python
# Correct:
import os
import sys

# Wrong:
import os, sys
```

### Import Order and Grouping
Put imports at the top of the file (after any module docstring). Group them in the order: 1) standard library, 2) third-party, 3) local application/library imports. Insert a blank line between each group. For example:

```python
import os  # Standard library
import sys

import numpy as np  # Third-party

from mypackage import utils  # Local application
```

### Absolute Imports
Prefer absolute imports for clarity (e.g. `import mypkg.module`). Relative imports (`from . import sibling`) are allowed in complex packages.

### Avoid Wildcards
Do not use `from module import *`; it obscures which names are present.

## Whitespace Usage

PEP 8 discourages extraneous spaces to reduce visual clutter. Key rules include:

### Inside Brackets
No spaces immediately inside parentheses, brackets or braces.

```python
# Correct:
spam(ham[1], {eggs: 2})

# Wrong:
spam( ham[ 1 ], { eggs: 2 } )
```

### Around Punctuation
Do not put a space before a comma, semicolon or colon; put one space after each comma. Also no space before a colon in slicing or indexing.

```python
# Correct:
if x == 4: print(x, y); x, y = y, x

# Wrong:
if x == 4 : print(x , y) ; x , y = y , x
```

### Around Operators
Use a single space around assignment (`=`), comparisons (`==`, `<`, `>=`, etc.), and arithmetic operators. Do not align code by adding extra spaces around operators.

```python
# Correct:
x = 1
y = 2
long_variable = 3

# Wrong (aligned for visual effect):
x             = 1
y             = 2
long_variable = 3
```

## Comments and Docstrings

### Block Comments
Use `#` for comments on their own line, aligned with the code they describe. Start with `#` (one space after `#`).

### Inline Comments
Use sparingly. Inline comments should be separated by at least two spaces from the statement and start with `#`. They should explain "why," not "what" (avoid obvious remarks).

```python
# Correct:
# Compute corrected value accounting for calibration offset.
value = raw_value * 0.98  # calibration adjustment

# Wrong:
x = x + 1  # increment x
```

### Docstrings
Use triple double-quotes (`"""like this"""`) for docstrings. Write docstrings for all public modules, classes, functions, and methods. The closing `"""` should be on its own line for multi-line docstrings. For example:

```python
# Correct:
def add(a, b):
    """Return the sum of a and b."""
    return a + b

# Wrong:
def add(a, b):
    '''Return the sum of a and b.'''  # Incorrect quoting/style
    return a + b
```

## Function and Class Definitions

### Blank Lines
Surround top-level class and def definitions with two blank lines, and methods inside a class with one blank line.

```python
# Correct:
class A:
    pass


class B:
    pass


def foo():
    pass

# Wrong (missing blank lines):
class A:
    pass
class B:
    pass
def foo():
    pass
```

### Method Separation
Inside a class, put one blank line between method definitions.

```python
# Correct:
class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass

# Wrong:
class MyClass:
    def method_one(self):
        pass
    def method_two(self):
        pass
```

### Method Arguments
Always use `self` as the first parameter of instance methods and `cls` for class methods.

### Naming Methods
Follow function naming rules (snake_case) for methods. Prefix a single underscore for non-public methods/attributes (double underscore invokes name mangling).

## Line Length and Continuations

### Maximum Line Length
Limit all code lines to 79 characters (docstrings/comments to 72).

### Implicit Continuation
Prefer wrapping long expressions inside parentheses, brackets or braces rather than using a backslash.

### Breaking Expressions
When breaking long expressions, it can be clearer to break before binary operators so that operators line up vertically. For example:

```python
# Correct (implicit line continuation):
total = (first_var
         + second_var
         - third_var)

# Wrong (line too long or backslash):
total = first_var + second_var - third_var  # exceeds 79 chars
```

## Readability Best Practices

Python's guiding principle is that "Readability counts." Write code for humans first: use clear logic, meaningful names, and simple constructs. For example:

### Use descriptive names
Prefer `calculate_mean` over `calc` or `x`.

### Be explicit
When checking for `None`, use `is`/`is not` rather than equality.

```python
# Correct:
if result is not None:
    ...

# Wrong:
if not result is None:
    ...
```

### Prefer def over lambda for named functions
This gives the function a proper name in tracebacks and readability.

```python
# Correct:
def square(x):
    return x * x

# Wrong:
square = lambda x: x * x
```

### Consistent style
Once you choose a style (e.g. indent, naming), stick to it throughout a project. It's better to follow project-specific conventions if they exist.

Adhering to these PEP 8 conventions helps maintain clean, consistent, and professional code across data science, AI, and software projects.