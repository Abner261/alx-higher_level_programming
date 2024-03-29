### 0x0C. Python - Almost a circle

### Background Context
- The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

##### In this project, you will review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

##### You will also learn about:

- <code>args</code> and <code>kwargs</code>
- Serialization/Deserialization
- JSON

### Resources
#### Read or watch:

- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

### Learning Objectives

- At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google

#### General
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is <code>*args</code> and how to use it
- What is <code>**kwargs</code> and how to use it
- How to handle named arguments in a function

### Description of what each file shows (Tasks):
- **main**	---> folder that holds all main.py files provided as test cases.
- **models**	---> folder that holds the main projects functions for submission
- **tests**	---> folder that contains all testcase file for functions written (Unittest module)

### Requirements
#### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle `(version 2.8.*)`
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)' `and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start with `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
- We strongly encourage you to work together on test cases so that you don’t miss any edge case

#### [0] If it's not tested it doesn't work

- All your files, classes and methods must be unit tested and be PEP 8 validated



Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor``````: def __init__(self, id=None):`:
- if `id`is not `None`, assign the public instance attribute `id` with this argument value - you can assume id is an integer and you don’t need to test the type of it
- otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`
- This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

##### [2]Write the class `Rectangle` **that inherits from** `Base`:

- In the file `models/rectangle.py`
- Class `Rectangle` inherits from `Base`
- Private instance attributes, each with its own public getter and setter:
- __width -> `width`
- `__height` -> `height`
- `__x` -> `x`
- `__y` -> `y`
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None)`:
- Call the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
- Assign each argument `width`, `height`, `x` and `y` to the right attribute
- Why private attributes with getter/setter? Why not directly public attribute?

- Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.

##### [3]Update the class Rectangle by adding validation of all setter methods and instantiation (`id` excluded):

- If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
- If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
- If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`
