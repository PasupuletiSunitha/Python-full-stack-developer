Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#join[which is used to join]
a="gnt vij hyd"
"s".join(a)
'gsnsts svsisjs shsysd'
"".join(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    "".join(b)
NameError: name 'b' is not defined
"".join(a)
'gnt vij hyd'
#concatenation[adding two strings]
a="sunitha"
b="pasupuleti"
print(a+b)
sunithapasupuleti
print(a+" "+b)
sunitha pasupuleti
print(fname+lname)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(fname+lname)
NameError: name 'fname' is not defined
fname="sunitha"
lname="pasupuleti"
SyntaxError: multiple statements found while compiling a single statement
fname="sunitha"
lname="pasupuleti"
print(fname+lname)
sunithapasupuleti
print(fname+" "+lname)
sunitha pasupuleti
print(fname.title()+" "+lnmae.title())
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(fname.title()+" "+lnmae.title())
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
print(fname.title()+" "+lname.title())
Sunitha Pasupuleti
>>> #format method
>>> a=4
>>> b=8
>>> print(a+b)
12
>>> print("the sum is ",a+b)
the sum is  12
>>> x="vja"
>>> print("city is",x)
city is vja
>>> a="motu"
>>> b="patlu"
>>> print("hello",a+b)
hello motupatlu
>>> print("hello{}{}".format(a,b))
hellomotupatlu
>>> print("hello{} {}".format(a,b))
hellomotu patlu
>>> print("hello{} hello{}".format(a,b))
hellomotu hellopatlu
>>> #fstring
>>> a="sita"
>>> b="rama"
>>> print(f"hello {a}[b}")
SyntaxError: f-string: single '}' is not allowed
>>> print(f"hello {a}{b}")
hello sitarama
>>> a="23"
>>> b="45"
>>> print("the product is ",a*b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print("the product is ",a*b)
TypeError: can't multiply sequence by non-int of type 'str'
>>> a=23
>>> b=46
>>> print("the product is ",a*b)
the product is  1058
>>> print(f"the product is {c}")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(f"the product is {c}")
NameError: name 'c' is not defined
>>> c=a*b
>>> print(f"the product is {c}")
the product is 1058
