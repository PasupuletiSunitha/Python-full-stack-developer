Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple and tuple methods
>>> a=(4,5.6,"suni",5+9j,True,False)
>>> type(a)
<class 'tuple'>
>>> a.count(5+9j)
1
>>> a.index(True)
4
>>> len(a)
6
>>> #sets
>>> a={2,3.9,"suni",5+9j,True,False}
>>> print(a)
{False, True, 2, 3.9, (5+9j), 'suni'}
>>> type(a)
<class 'set'>
>>> a={3,4,5,6,7,8}
>>> b={5,6,7,8}
>>> b.issubset(a)
True
>>> b.issubset(b)
True
>>> #superset
>>> a.issuperset(b)
True
>>> a.issuperset(a)
True
>>> #union-merging of two elements
>>> a.union(b)
{3, 4, 5, 6, 7, 8}
>>> c={1,2,3,4,5,6,7,8}
>>> c
{1, 2, 3, 4, 5, 6, 7, 8}
>>> #intersection-it will prints common elements
>>> a.intersection(b)
{8, 5, 6, 7}
>>> a
{3, 4, 5, 6, 7, 8}
>>> #update
>>> a.update(b)
>>> a
{3, 4, 5, 6, 7, 8}
>>> a={3,4,5,6,7,8}
>>> b={5,6,7,8}
a.update(b)
a
{3, 4, 5, 6, 7, 8}
b
{8, 5, 6, 7}
#difference
#difference
a={1,2,3,4,5,6}
b={3,4,5,6,7,8,9,0}
a.difference(b)
{1, 2}
b.difference(a)
{0, 8, 9, 7}
#symmetric difference
a.symmetric_difference(b)
{0, 1, 2, 7, 8, 9}
b.symmetric_difference(a)
{0, 1, 2, 7, 8, 9}
#intersection update
a.intersection_update(b)
a
{3, 4, 5, 6}
b.intersection_update(a)
b
{3, 4, 5, 6}
#difference_update
a.difference_update(b)
a
set()
a={2,3,4,5,6,7}
b={1,2,3,4,5,6,7}
a.difference_update(b)
a
set()
a={11,12,13,14,15,16,17}
b={13,14,15,16,17,18}
a.symmetric_difference_update(b)
a
{18, 11, 12}
a
{18, 11, 12}
b.symmetric_difference_update(a)
b
{16, 17, 11, 12, 13, 14, 15}
a.pop()
18
a.remove()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.remove()
TypeError: set.remove() takes exactly one argument (0 given)
a.remove(5)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.remove(5)
KeyError: 5
a={3,4,5,6,7,8,9}
a.copy()
{3, 4, 5, 6, 7, 8, 9}
a
{3, 4, 5, 6, 7, 8, 9}
a.clear()
a
set()
b=set()
b.add(20)
b
{20}
len(a)
0
a.isdijoint(b)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.isdijoint(b)
AttributeError: 'set' object has no attribute 'isdijoint'. Did you mean: 'isdisjoint'?
