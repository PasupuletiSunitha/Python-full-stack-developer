Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#bitwise operators
a&b
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a&b
NameError: name 'a' is not defined
a=5
b=7
a&b
5
bin(2)
'0b10'
bin(4)
'0b100'
bin(5)
'0b101'
bin(7)
'0b111'
a=3
b=5
a|b
7
a=5
b=9
a|b
13
#not
a=5
-(a+1)
-6
~a
-6
a=9
~a
-10
b=-9
~b
8
c=-12
~c
11
>>> #xor
>>> a^b
-2
>>> a=7
>>> b=7
>>> a^b
0
>>> c=23
>>> d=65
>>> a^b
0
>>> c^d
86
>>> #left shift,right bshift
>>> a=3
>>> a<<2
12
>>> b=4
>>> a<<3
24
>>> b<<3
32
>>> #right shift
>>> a=5
>>> a>>2
1
>>> a=8
>>> a>>5
0
>>> a=12
>>> a>>6
0
>>> #left shift
>>> a=8
>>> a<<5
256
>>> a=234
>>> a<<200
376023502356603724476819129607832048990195500545173523460521984
>>> a=1234567083645368
>>> a<<23458
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a<<23458
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
