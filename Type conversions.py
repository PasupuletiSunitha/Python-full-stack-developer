Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int
>>> int(23.0)
23
>>> int("code")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("code")
ValueError: invalid literal for int() with base 10: 'code'
>>> int(True)
1
>>> #float
>>> float(23)
23.0
>>> float("python")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
>>> float(4+9j)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    float(4+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> #string
>>> string(12)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    string(12)
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> string("4.5")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    string("4.5")
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> string("4+9j")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    string("4+9j")
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> string(23.0)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    string(23.0)
NameError: name 'string' is not defined. Did you forget to import 'string'?
str("codegnan")
'codegnan'
str(23.0)
'23.0'
str(4+9j)
'(4+9j)'
str(True)
'True'
str(3j+6)
'(6+3j)'
#complex
complex(23)
(23+0j)
complex(4.5)
(4.5+0j)
complex("python")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
#boolean
bool(23)
True
bool(23.0)
True
bool("python")
True
bool(4+9j)
True
bool(True)
True
bbol(1)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    bbol(1)
NameError: name 'bbol' is not defined. Did you mean: 'bool'?
bool(1)
True
bool(0)
False
