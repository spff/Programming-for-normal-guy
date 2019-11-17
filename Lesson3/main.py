# equals to class Animal(object):
class Animal():
    # __init__ is a special function~
    def __init__(self, legs=0, name='Animal'):
        print(f'Animal __init__')
        self.legs = legs
        self.name = name
    
    def bark(self):
        return f'I\'m a {self.name}, I have {self.legs} legs'

    # override the __str__ of object
    def __str__(self):
        return self.bark()

# the Wolf inherit Animal
class Wolf(Animal):
    def __init__(self, color):
        print(f'Wolf __init__')
        super().__init__(legs=4, name='Wolf')
        # attribute of Wolf, but not Animal
        self.color = color

    def __str__(self):
        return f'{super().__str__()}, I\'m {self.color}'

animal = Animal()
print(animal.name)
print(animal.bark())
print(str(animal))
print(f'{animal}')
print('see~ the above f\'{XXX}\' is actually f\'{str(XXX)}\'')
print(f'animal is {type(animal)}, and by observing {type.mro(Animal)}, the Animal inherit object, as line #1 mentioned')

animal = Animal(legs=5)
print(str(animal))
print()

wolf = Wolf('gray')
print(wolf.color)
print(str(wolf))
print(f'{type.mro(Wolf)}')

print()

print(f'''
because Wolf inherit Animal, and Animal inherit object,
isinstance(wolf, Animal)={isinstance(wolf, Animal)}
isinstance(wolf, object)={isinstance(wolf, object)}
isinstance(animal, Wolf)={isinstance(animal, Wolf)}
issubclass(type(animal), Animal)={issubclass(type(animal), Animal)}
''')

input('\n########## line 54 ##########\n')

a = Animal(legs=8)
b = a
b.legs=9
print(f'{a}, and {b}')

input('\n########## line 61 ##########\n')

try:
    a = 1 / 0
except Exception as e:
    err_msg = e.args[0]
    print(f'e={e}, it\'s a {type(e)}, err_msg={err_msg}')
finally:
    print('finally')
print()
# the try requires at least one `except` or `finally`

try:
    a = 1 / 0
    print('hi')
except Exception as e:
    err_msg = e.args[0]
    print(f'{err_msg}, it\'s a {type(e)}, isinstance(e, Exception)={isinstance(e, Exception)} because the inherit chain of e\'s type is {type.mro(type(e))}')
print()

try:
    try:
        raise Exception('my exception')
        print('hi')
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError')
    # if there is any Exception which haven't been catched by `except`, it'll raise to the outer scope
    finally:
        print('finally')
except Exception as e:
    err_msg = e.args[0]
    print(err_msg)
print()

class MyCuteException(Exception):
    def __init__(self):
        self.args = ['I am cute XDD']

try:
    raise MyCuteException()
except Exception as e:
    print(e.args[0])
print()

try:
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        print('catch e, and reraise')
        raise e
except Exception as e:
    err_msg = e.args[0]
    print(err_msg)
print()

try:
    try:
        a = 1 / 0
    finally:
        print('finally')
except Exception as e:
    err_msg = e.args[0]
    print(err_msg)
print()

try:
    raise ZeroDivisionError()
# For multiple `except`, Python will 
except ZeroDivisionError as e:
    print('catch ZeroDivisionError')
except Exception as e:
    print('catch Exception')
print()

try:
    raise ZeroDivisionError()
    # if there is any Exception which haven't been catched by `except`, it'll raise to the outer scope
except Exception as e:
    print('catch Exception')
except ZeroDivisionError as e:
    print('catch ZeroDivisionError')


input('\n########## line 144 ##########\n')

print('In lesson2, we found the elements are mutable in list')
a = []
b = a
b.append(5)
print(f'a={a}, b={b}')

print('we got 2 approaches to prevent someone to mutate the content')
print('1. construct a new one, using [:] or consntructor `list()`')
c = a[:]
d = list(c)

c.clear()
d.append('q')

print(f'a={a}, b={b}, c={c}, d={d}')
print('\n2. using tuple instead of list which is immutable, so we don\'t need to keep two copies of the same contents in computer\'s memory(RAM)')
a = [1,2,3]
a = tuple(a)
print(f'a={a}')
# or just directly construct a tuple by
a = (1,2,3)
print(f'a={a}')
try:
    a[1] = 5
except TypeError as e:
    print(str(e))
try:
    a.clear()
except AttributeError as e:
    print(f'{e}, just cannot modify any content of the tuple')
print()
print('You should keep in mind this only works on the first level, no matter you apply which approach')
a = (1, ['a', 'b'], 1)
b = list(a)
c = a[:]
print(f'a={a}, b={b}, c={c}')
a[1][0] = 'A'
print(f'a={a}, b={b}, c={c}')

print('''
          /------['a', 'b']
a => (1, /, 1)  / /
          /----/ /
b => [1, /, 1]  /
          /----/
c => [1, /, 1]
''')
print('all the approach mention above is called shallow copy')
print('for deep copy, we use copy.deepcopy()')
import copy
aa = copy.deepcopy(a)
print(f'aa={aa}, a={a}')
a[1][1] = 'B'
print(f'aa={aa}, a={a}')
print('''
a => (1, ['A', 'B'], 1)
aa=> (1, ['A', 'b'], 1)
''')



input('\n########## line 207 ##########\n')


# {} is a dict(tionary), which stores data in key:value structure
a = {}
print(f'a is {a}. it\'s a {type(a)}, it\'s empty, so it\'s length is {len(a)}')
a['A'] = 'AA'
print(f'now a is {a}, it\'s length is {len(a)}')
a['B'] = 'BB'
print(f'now a is {a}, it\'s length is {len(a)}')
print(f''' is 'c' in a: {'c' in a}''')
print(f'''try get 'c' in a {a.get('c')}, default is None''')
print(f'''try get 'c' in a {a.get('c', 666)}''')
a['c'] = 'CC'
print(f''' is 'c' in a: {'c' in a}''')
print(f'now a is {a}, it\'s length is {len(a)}')
b = a
print(f'now a is {a}, b is {b}')
b['c'] = 'CCC'
print(f'now a is {a}, b is {b}')
print('Both b and a are referencing to the same dict')

input('\n########## line 229 ##########\n')

for key in b:
    print(key)
print()
for key in b.keys():
    print(key)
print()
for value in b.values():
    print(value)
print()
for item in b.items():
    print(f'item={item}, it\'s a {type(item)}, with the first element as key={item[0]}, and the second element as value={item[1]}')
print()
print('we can unpack the tuple')
print('''
In Python 3.7.0 the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.
Therefore, you can depend on it.
https://stackoverflow.com/questions/5629023/the-order-of-keys-in-dictionaries
''')
for k, v in b.items():
    print(f'k={k}, v={v}')

input('\n########## line 252 ##########\n')

a = list(range(10))
print(a)
a = tuple(a)
print(a)
a = list(a)
print(a)
a = { x*x: x*(-10) for x in a }
print(a)
a = [ str(x) for x in a.values() ]
print(a)
a = [ len(x) for x in a ]
print(a)
a = set(a)
print(a)
a.add('7')
print(f'a={a}')
b = set([1,2,3])
print(f'b={b}, a|b={a|b}, a&b={a&b}, a-b={a-b}, b-a={b-a}')

input('\n########## line 273 ##########\n')

from lib.my_first_lib import lib1
print(lib1.a)
print(lib1.hi())


def am_i_main():
    return __name__ == '__main__'

print(f'main:{am_i_main()}, lib1:{lib1.am_i_main()}')

a = 0
def normal_func():
    a = 5
    def inner_func(a):
        return a+1
    print(a)
    return inner_func(8)
print(a)
print(normal_func())
print(a)
print()

def modify_global():
    global a
    a = 5

print(a)
print(modify_global())
print(a)
print()

def f1():
    a = 5
    def inner_func():
        a = 10
        return a
    print(inner_func())
    return a

print(a)
print(f1())
print(a)
print()

def f2():
    a = 5
    def inner_func():
        nonlocal a
        a = 10
        return a
    print(inner_func())
    return a

print(a)
print(f2())
print(a)

input('\n########## line 332 ##########\n')
a = { 'a': {'age': 10}, 'b': {'age': 8}, 'c': {'age': 50} }

print(list(a.items()))
print(sorted(list(a.items())))
print(sorted(list(a.items()), reverse=True))
def get_age(x):
    print(x)
    return x[1]['age']
print(sorted(list(a.items()),key=get_age))
print(sorted(list(a.items()),key=lambda x: x[1]['age']))

double = lambda x: x*2
print(double(5))

def func_double(x):
    return x*2

print(func_double(5))

def factorial(n):
    if n < 1:
        raise Exception()
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def factorial_iter(n):
    if n < 1:
        raise Exception()
    ret = 1
    for x in range(n, 1, -1):
        ret *= x
    return ret

print(factorial_iter(5))
print()

def nothing():
    pass
print(nothing())

print()
def cf(a=0):
    while True:
        a += 1
        print(a)
        if a > 10:
            return 'QQ'
        elif a % 2 == 0:
            continue
        elif a % 3 == 0:
            pass
        else:
            a += 1
    else:
        return 'yee'
    return 'yo'

print(cf(0))
print()
print(cf(1))