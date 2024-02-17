#### 0x09. Python - Everything is object

#### Resources
##### Read or watch:

- https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values
- https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing
- https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types
- https://www.composingprograms.com/pages/24-mutable-data.html
- https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists
- http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html

#### General

- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

#### Requirements

##### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a newline character
- The first line of all your script files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

#### .txt Answer Files

- Only one line
- No Shebang
- All your files should end with a new line

##### [0]What function would you use to get the type of an object?

- Write the name of the function in the file, without ().

##### [1]How do you get the variable identifier (which is the memory address in the CPython implementation)?

- Write the name of the function in the file, without ().

##### [2]In the following code, do a and b point to the same object? Answer with Yes or No.

- >>> a = 89
- >>> b = 100

##### [3]In the following code, do a and b point to the same object? Answer with Yes or No.

- >>> a = 89
- >>> b = 89

##### [4]In the following code, do a and b point to the same object? Answer with Yes or No.

- >>> a = 89
- >>> b = a

##### [5]In the following code, do a and b point to the same object? Answer with Yes or No.

- >>> a = 89
- >>> b = a + 1

##### [6]What do these 3 lines print?

- >>> s1 = "Best School"
- >>> s2 = s1
- >>> print(s1 == s2)

##### [7]What do these 3 lines print?

- >>> s1 = "Best"
- >>> s2 = s1
- >>> print(s1 is s2)

##### [8]What do these 3 lines print?

- >>> s1 = "Best School"
- >>> s2 = "Best School"
- >>> print(s1 == s2)

##### [9]What do these 3 lines print?

- >>> s1 = "Best School"
- >>> s2 = "Best School"
- >>> print(s1 is s2)

##### [10]What do these 3 lines print?

- >>> l1 = [1, 2, 3]
- >>> l2 = [1, 2, 3] 
- >>> print(l1 == l2)

##### [11]What do these 3 lines print?

- >>> l1 = [1, 2, 3]
- >>> l2 = [1, 2, 3] 
- >>> print(l1 is l2)

##### [12]What do these 3 lines print?

- >>> l1 = [1, 2, 3]
- >>> l2 = l1
- >>> print(l1 == l2)

##### [13]What do these 3 lines print?

- >>> l1 = [1, 2, 3]
- >>> l2 = l1
- >>> print(l1 is l2)

##### [14]What does this script print?

- l1 = [1, 2, 3]
- l2 = l1
- l1.append(4)
- print(l2)

##### [15]What does this script print?

- l1 = [1, 2, 3]
- l2 = l1
- l1 = l1 + [4]
- print(l2)

##### [16]What does this script print?

- def increment(n):
- n += 1

- a = 1
- increment(a)
- print(a)

##### [17]What does this script print?

- def increment(n):
- n.append(4)

- l = [1, 2, 3]
- increment(l)
- print(l)

##### [18]What does this script print?

- def assign_value(n, v):
- n = v

- l1 = [1, 2, 3]
- l2 = [4, 5, 6]
- assign_value(l1, l2)
- print(l1)

##### [19]Write a function def copy_list(l): that returns a copy of a list.

- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module

##### [20]Is a a tuple? Answer with Yes or No.

- a = ()

##### [21]Is a a tuple? Answer with Yes or No.

- a = (1, 2)

##### [22]Is a a tuple? Answer with Yes or No.

- a = (1)

##### [23]Is a a tuple? Answer with Yes or No.

- a = (1, )

##### [24]What does this script print?

- a = (1)
- b = (1)
- a is b

##### [25]What does this script print?

- a = (1, 2)
- b = (1, 2)
- a is b

##### [26]What does this script print?

- a = ()
- b = ()
- a is b

##### [27]Will the last line of this script print 139926795932424? Answer with Yes or No.

- >>> id(a)
- 139926795932424
- >>> a
- [1, 2, 3, 4]
- >>> a = a + [5]
- >>> id(a)

##### [28]Will the last line of this script print 139926795932424? Answer with Yes or No.

- >>> a
- [1, 2, 3]
- >>> id (a)
- 139926795932424
- >>> a += [4]
- >>> id(a)

##### [29]Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):

- Format: see example
- Your file should be maximum 4-line long (no documentation needed)
- You are not allowed to import any module

##### [30]Write a class LockedClass with no class or object attribute,
##### that prevents the user from dynamically creating new instance attributes,
##### except if the new instance attribute is called first_name.

- You are not allowed to import any module

##### [31]Assuming we are using a CPython implementation of Python3 with default options/configuration:

- How many int objects are created by the execution of the first line of the script? (103-line1.txt)
- How many int objects are created by the execution of the second line of the script (103-line2.txt)
- a = 1
- b = 1

##### [32]Assuming we are using a CPython implementation of Python3 with default options/configuration:

- How many int objects are created by the execution of the first line of the script? (104-line1.txt)
- How many int objects are created by the execution of the second line of the script (104-line2.txt)
- After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
- After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
- How many int objects are created by the execution of the last line of the script (104-line5.txt)
- a = 1024
- b = 1024
- del a
- del b
- c = 1024

##### [33]Assuming we are using a CPython implementation of Python3 with default options/configuration:

- Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
- Why? (optional blog post :))
- Hint: NSMALLPOSINTS, NSMALLNEGINTS
- print("I")
- print("Love")
- print("Python")

##### [34]Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

- How many string objects are created by the execution of the first line of the script? (106-line1.txt)
- How many string objects are created by the execution of the second line of the script (106-line2.txt)
- After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
- After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
- How many string objects are created by the execution of the last line of the script (106-line5.txt)
- a = "SCHL"
- b = "SCHL"
- del a
- del b
- c = "SCHL"


