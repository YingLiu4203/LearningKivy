# Python Review
## Getting Help
The `help()` built-in function to get help for an object. 
The `dir()` built-in function lists all attributes of an object.
The `type()` built-in function is used to find the type of an object.
The `id()` built-in function returns the identity, an integer, of 
an object. Usually it is the memory address of the object.
The `__doc__` attribute displays the docstring of an object. 

In ipython interpreter, get help for an object by placing `?` after
an object. 

## Data Types
Python is implicitly typed in the sense that there is no need 
to declare a type for a variable. However, a values or a 
variable still has a type that determines the types of operations
can be used. 

Python provides many built-in data types including numbers, strings, lists, 
dictionaries, tuples, sets, files, etc. Developers create new data types
using class definitions. 

### Numbers
Number types include int, float, and even complex numbers. One can 
convert a value to an integer value using `int()`, to a float value
using `float()`. The result of a division of two integers is an integer. 
For example, the result of `2 / 7` is 0 and the result of `7 / 2` is 3. 

### Strings
A string is a sequence of characters. A string object supports index slicing
and other methods as shown below. The `str()` built-in 
function is used to convert an object to a string.

```python
s1 = "hello world"
s2 = s1[1]      # 'e'
s3 = s1[-1]     # 'd'
s4 = s1[1:5:2]  # 'el'
len(s1)         # the length of a string
index = s.find('world')     # index is 6
index2 = s.find('World')    # index is -1, not found
s5 = s.replace('world', 'python')   # s5 is 'hello python'
s6 = s.split()  # s6 is ['hello', 'world']
s7 = s.title()  # s7 is 'Hello World'
s8 = s.upper()  # s8 is 'HELLO WORLD'
```
A string is an immutable object, slicing or replacing a string 
returns a new string object. 


### Lists
A list is a sequence of elements. List elements can have different 
types. A list object supports indexing, slicing and other methods.
The `list()` is used to convert a sequence into a list. 

```python
demo = ['abc', 200, [1, 2, 3], "hello world"]
demo[0]     # 'abc'
demo[-1]    # "hello world'
demo[:2]    # ['abc', 200]
demo.append(18) # demo is ['abc', 200, [1, 2, 3], "hello world", 18]
demo.pop(3)     # demo is ['abc', 200, [1, 2, 3], 18]
demo[2][2]      # returns 3
demo[10]        # index out of range error
200 in demo     # True
300 in demo     # False

demo[1] = 'abc'     # demo is ['abc', 'abc', [1, 2, 3], 18]
demo.count('abc')   # returns 2
demo.index('abc')   # returns 0 -- the index of the first 'abc'
demo.index(18)      # returns 3

demo2 = list('hello')   # ['h', 'e', 'l', 'l', 'o']
del demo[:]     # delete all demo elements. demo is []
demos[:] = []    # delete all demo2 elements
```

### Dictionaries
Python dictionaries are mappings that map unique keys to their values.
A dictionary can be declared in two ways. 

```python
d1 = {'title': 'Mr.', 'name': 'bob', 'age': 20,}
d2 = dict(title='Mr.', name='bob', age=20)
d1 == d2        # True
d1 is d2        # False
d3 = d1         # d3 is a new variable to d1
d3 is d1        # True

d1['title']     # returns 'Mr.'
d1['Title']     # returns a KeyError exception
d1.get('Title') # returns None
d1.get('Title', 'Not Found')    # returns 'Not Found'
'title' in d1   # True

d1.keys()       # returns ['age', 'name', 'title']
d1.values()     # returns [20, 'bob', 'Mr.']

d1['title'] = 'Ms.' # d1 is {'age':20, 'name': 'bob', 'title': 'Ms.'}
d1.pop('title') # d1 is {'age':20, 'name': 'bob'}
d1.clear()      # d1 is {}
```

### Tuples
A tuple is a sequence of elements, like a list, but it is immutable. 
Once defined, it can not be changed. A tuple object supports 
the most list methods except those methods that change list elements. 
The `tuple()` function converts a sequence into a tuple.

```python
t1 = (1, 'abc')
t2 = ('abc', )  # a single element tuple
t3 = ('abc')    # t3 is a string
t1[0] = 2       # TypeError exception, a tuple is immutable
```
### Sets
A set is a collection of unique elements, i.e., each element 
only appears once in a set. A set object can be defined using
the `set()` function or a set literal.  

```python
s1 = set([1, 2, 3, 4])
s2 = {1, 3, 5, 7}
2 in s1     # True
2 in s2     # False
s1.add(2)   # s1 still is {1, 2, 3, 4}
s2.add(2)   # s2 becomes {1, 2, 3, 5, 7}
s3 = s1 - s2    # s3 is {4}
s4 = s2 - s1    # s4 is {5, 7}
s5 = s1.union(s2)    # s5 is {1, 2, 3, 4, 5, 7}


## Functions


## Classes
Python allows developers to define new object types using class. 
To use new Python features, all new classes should be defined 
as a subclass of `object`. 















