Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operators
#arithmeti
a=10
b=20
print(a+b)
30
print(a-b)
-10
print(a*b)
200
print(a//b)
0
print(a/b)
0.5
print(a**b)
100000000000000000000
print(a%b)
10
print(b%a)
0
print(b-a)
10
#Assignment Operators
a=3
b=5
5+=3
SyntaxError: 'literal' is an illegal expression for augmented assignment
a+b
8
b+=a
b
8
print(b)
8
b-=a
b
5
b*=a
print(b)
15
b/=a
b
5.0
b//=a
b
1.0
b%=a
b
1.0
#Comparision Operators
a=23
b=34
a<b
True
a>b
False
a==b
False
a<=b
True
a>=b
False
a!=b
True
b<a
False
b>a
True
b==a
False
b<=a
False
b>=a
True
>>> b!=a
True
>>> #lLogical Operators
>>> a=3
>>> b=6
>>> a<b and b>a
True
>>> a<=b and b>=a
True
>>> a!=b or b>a
True
>>> <=b or b<=a
SyntaxError: invalid syntax
>>> a<=b or b<=a
True
>>> a!=b
True
>>> a!=b 0r b<=a
SyntaxError: invalid decimal literal
>>> #identity operators
>>> a=4
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> type(a) is int
True
>>> type(b) is int
True
>>> type(a) is not str
True
>>> #Membership Operators
>>> a=1,2,3,4,5,6,7,8,9,o
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a=1,2,3,4,5,6,7,8,9,o
NameError: name 'o' is not defined
>>> a=1,2,3,4,5,6,7,8,9,0
>>> 1 in a
True
>>> 22  not in a
True
>>> a=4
>>> 
>>> #logical not
