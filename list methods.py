Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=5
type(c)
<class 'int'>
a=['python','java','c','c++','DSA']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
#extend()
a=["ml","ai","ds"]
a.extend(["c","c++","python"])
a
['ml', 'ai', 'ds', 'c', 'c++', 'python']
#insert()
b=["vij","hyd"]
b.insert(1,"vzg")
b
['vij', 'vzg', 'hyd']
#index
a=["black","white","pink","red"]
a.index("white")
1
a.copy()
['black', 'white', 'pink', 'red']
b
['vij', 'vzg', 'hyd']
b.count("pink")
0
b=a.copy()
b
['black', 'white', 'pink', 'red']
b.count("pink")
1
#sort
a=["grapes","apple","lichi","jackfruit"]
a.sort()
a
['apple', 'grapes', 'jackfruit', 'lichi']
b=[3,4,8,0,1,2,56]
b.sort()
b
[0, 1, 2, 3, 4, 8, 56]
#reverse
>>> a=[1,2,54,34,67]
>>> a.reverse()
>>> a
[67, 34, 54, 2, 1]
>>> b=["java","html","css"]
>>> b.reverse()
>>> b
['css', 'html', 'java']
>>> #pop
>>> a=['c','c++','ml']
>>> a.pop()
'ml'
>>> a
['c', 'c++']
>>> #remove
>>> #remove
>>> a.remove("ml")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.remove("ml")
ValueError: list.remove(x): x not in list
>>> a.pop(1)
'c++'
>>> a
['c']
>>> a.remove("ml")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.remove("ml")
ValueError: list.remove(x): x not in list
>>> a
['c']
>>> #len
>>> a=["sunitha","srujana","vijji","yashu"]
>>> len(a)
4
>>> c="sunitha"
>>> len(c)
7
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
