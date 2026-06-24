Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
#starts with a letter or underscore
a=10
print(a)
10
name=("sunitha")
print(name)
sunitha
#concatenation
a=("sunitha")
b=("pasupuleti")
print(a+b)
sunithapasupuleti
>>> #dont use keywords
>>> _=22
>>> print("_")
_
>>> city="guntur"
>>> print(city)
guntur
>>> country="india"
>>> print(country)
india
>>> #doesnt allows special characters
>>> _suni="Good girl"
>>> print(_suni)
Good girl
>>> @a=40
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> mailid=suni@gmail.com
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    mailid=suni@gmail.com
NameError: name 'suni' is not defined. Did you mean: '_suni'?
>>> mailid="suni@gmail.com"
>>> print(mailid)
suni@gmail.com
>>> #it doesnt allow keywords
>>> if=30
SyntaxError: invalid syntax
>>> elif=45
SyntaxError: invalid syntax
>>> print=10
>>> print(print)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(print)
TypeError: 'int' object is not callable
>>> a=4;b=7
>>> print(a,b)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(a,b)
TypeError: 'int' object is not callable
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(a+b)
TypeError: 'int' object is not callable
