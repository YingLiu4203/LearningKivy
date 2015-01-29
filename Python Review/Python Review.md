# Python Review
## Data Types
Python is implicitly typed in the sense that there is no need 
to declare a type for a variable. However, a values or a 
variable still has a type that determines the types of operations
can be used. 

Python provides many built-in data types including numbers, strings, lists, 
dictionaries, tuples, sets, files, etc. Developers create new data types
using class definitions. The `type()` built-in function is used to find
the type of a value or a variable. 

Number types include int, float, and even complex numbers. One can 
convert a value to an integer value using `int()`, to a float value
using `float()`. The result of a division of two integers is an integer. 
For example, the result of `2 / 7` is 0 and the result of `7 / 2` is 3. 

A string is a sequence of characters. A string supports index slicing.

```python
s1 = "hello world"
s2 = s1[1]      # 'e'
s3 = s1[-1]     # 'd'
s4 = s1[1:5:2]  # 'el'
```


