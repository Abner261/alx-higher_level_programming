#### 0x05. Python - Exceptions

##### [0]Write a function that prints x elements of a list.

[a]Prototype: def safe_print_list(my_list=[], x=0):
[b]my_list: can contain any type (integer, string, etc.)
[c]All elements must be printed on the same line followed by a new line.
[d]x: represents the number of elements to print
[e]x: can be bigger than the length of my_list
[f]Returns the real number of elements printed
[g]You have to use try: / except:
[h]You are not allowed to import any module
[i]You are not allowed to use len()

##### [1]Write a function that prints an integer with "{:d}".format().

[a]Prototype: def safe_print_integer(value):
[b]value: can be any type (integer, string, etc.)
[c]The integer should be printed followed by a new line
[d]Returns: True if value has been correctly printed (it means the value is an integer)
[e]Otherwise, returns False
[f]You have to use try: / except:
[g]You have to use "{:d}".format() to print as integer
[h]You are not allowed to import any module
[i]You are not allowed to use type()

##### [2]Write a function that prints the first x elements of a list and only integers.

[a]Prototype: def safe_print_list_integers(my_list=[], x=0):
[b]my_list: can contain any type (integer, string, etc.)
[c]All integers have to be printed on the same line followed
by a new line - other type of value in the list must be skipped (in silence).
[d]x: represents the number of elements to access in my_list
[e]x: can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
[f]Returns the real number of integers printed
[g]You have to use try: / except:
[h]You have to use "{:d}".format() to print an integer
[i]You are not allowed to import any module
[j]You are not allowed to use len()

##### [3]Write a function that divides 2 integers and prints the result.

[a]Prototype: def safe_print_division(a, b):
[b]You can assume that a and b are integers
[c]The result of the division should print on the finally: section preceded by Inside result:
[d]Returns the value of the division, otherwise: None
[e]You have to use try: / except: / finally:
[f]You have to use "{}".format() to print the result
[g]You are not allowed to import any module

##### [4]Write a function that divides element by element 2 lists.

[a]Prototype: def list_division(my_list_1, my_list_2, list_length):
[b]my_list_1 and my_list_2 can contain any type (integer, string, etc.)
[c]list_length can be bigger than the length of both lists
[d]Returns a new list (length = list_length) with all divisions
[e]If 2 elements can’t be divided, the division result should be equal to 0
[f]If an element is not an integer or float:
print: wrong type
[g]If the division can’t be done (/0):
print: division by 0
[h]If my_list_1 or my_list_2 is too short
print: out of range
[i]You have to use try: / except: / finally:
[j]You are not allowed to import any module

##### [5]Write a function that raises a type exception.

[a]Prototype: def raise_exception():
[b]You are not allowed to import any module

##### [6]Write a function that raises a name exception with a message.

[a]Prototype: def raise_exception_msg(message=""):
[b]You are not allowed to import any module

##### [7]Write a function that prints an integer.

[a]Prototype: def safe_print_integer_err(value):
[b]value can be any type (integer, string, etc.)
[c]The integer should be printed followed by a new line
[d]Returns True if value has been correctly printed (it means the value is an integer)
[e]Otherwise, returns False and prints in stderr the error precede by Exception:
[f]You have to use try: / except:
[g]You have to use "{:d}".format() to print as integer
[h]You are not allowed to use type()

##### [8]Write a function that executes a function safely.

[a]Prototype: def safe_function(fct, *args):
[b]You can assume fct will be always a pointer to a function
[c]Returns the result of the function,
[d]Otherwise, returns None if something happens during the
function and prints in stderr the error precede by Exception:
[e]You have to use try: / except:

##### [9]Write the Python function def magic_calculation(a, b):
##### that does exactly the same as the following Python bytecode:

##### [10]Create three C functions that print some basic info about Python lists
##### Python bytes an Python float objects

Python lists:

[a]Prototype: void print_python_list(PyObject *p);
[b]Format: see example
[c]If p is not a valid PyListObject, print an error message (see example)

Python bytes:

[a]Prototype: void print_python_bytes(PyObject *p);
[b]Format: see example
[c]Line “first X bytes”: print a maximum of 10 bytes
[d]If p is not a valid PyBytesObject, print an error message (see example)

Python float:

[a]Prototype: void print_python_float(PyObject *p);
[b]Format: see example
[c]If p is not a valid PyFloatObject, print an error message (see example)
[d]Read /usr/include/python3.4/floatobject.h

About:

[a]Python version: 3.4
[b]You are allowed to use the C standard library
[c]Your shared library will be compiled with this command line:
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,
libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
[d]You are not allowed to use the following macros/functions:
Py_SIZE
Py_TYPE
PyList_Size
PyList_GetItem
PyBytes_AS_STRING
PyBytes_GET_SIZE
PyBytes_AsString
PyBytes_AsStringAndSize
PyFloat_AS_DOUBLE
PySequence_GetItem
PySequence_Fast_GET_SIZE
PySequence_Fast_GET_ITEM
PySequence_ITEM
PySequence_Fast_ITEMS

NOTE:

[a]The python script will be launched using the -u option (Force stdout to be unbuffered).
[b]It is strongly advised to either use setbuf(stdout, NULL);
or fflush(stdout) in your C functions IF you choose to use printf.
The reason to that is that Pythonsprintand libCs printf don’t share
the same buffer, and the output can appear disordered.
