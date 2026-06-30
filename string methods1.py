Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count
#count=no.of repeated words
#we should give a variable
b="twinkle twinkle little star"
a.count("twinkle")
0

b'count("twinkle")
SyntaxError: unterminated string literal (detected at line 1)
b.count("twinkle")
2
b.count(a)
0
b.count(k)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b.count(k)
NameError: name 'k' is not defined
b.count("k")
2
#find a string
#if double letters present it is not possible,it is only present in slicing
c="code"
c.find a string("o")
SyntaxError: invalid syntax
c.find("c")
0
#escape sequence
#\n->newline \t->tab space[4-8]
a="name\nmobile no\tmailid\nclg"
print(a)
name
mobile no	mailid
clg
b="sunitha\n1234567890 no\tsuni@gmail.com\nst.marys"
print(b)
sunitha
1234567890 no	suni@gmail.com
st.marys
#replace
a="Hard work is the key to success"
a.replace("Hard","smart")
'smart work is the key to success'
a.replace("work","thinking")
'Hard thinking is the key to success'
#upper
a="pasupuleti sunitha"
a.upper()
'PASUPULETI SUNITHA'
b="visualization"
b.upper()
'VISUALIZATION'
c="PROCRASTINATION"
c.lower()
'procrastination'
c.capitalize()
'Procrastination'
b.capitalize()
'Visualization'
>>> #title is used to make starting letter of a word in asentence capital
>>> b.title()
'Visualization'
>>> e="suni is a good girl"
>>> e.capitalize()
'Suni is a good girl'
>>> #true and false conditions
>>> a="java"
>>> a.is upper()
SyntaxError: invalid syntax
>>> a.isupper()
False
>>> a.islower()
True
>>> b="python course"
>>> b.isalpha()
False
>>> c="pythoncourse"
>>> c.isdigit()
False
>>> c.isalnum()
True
>>> a="hello python"
>>> a.startswith("h")
True
>>> a.endswith("n")
True
>>> #strip[it is used to remove spaces]
>>> #lstrip,rstrip
>>> a="     sunitha     "
>>> a.strip()
'sunitha'
>>> a.lstrip()
'sunitha     '
>>> a.rstrip()
'     sunitha'
>>> #split[it is used to separate words]
>>> a="switzerland is a beautiful country"
>>> a.split()
['switzerland', 'is', 'a', 'beautiful', 'country']
>>> b="music is the best therapy"
>>> b.split()
['music', 'is', 'the', 'best', 'therapy']
>>> c="codegnan"
>>> c.split()
['codegnan']
