# this is a comment line

print('Hello World')
print("Hello World")
print('''
Hello
  World
    :D
''')
print(1)
print(1.1)
print(0xa)
print(f'1+1={1+1}')
print('1+1={the_sum}'.format(the_sum=1+1))
print('1+1={}, 2+2={}'.format(1+1, 2+2))
print()
s = input('type something\n')
print('you type {}'.format(s))


print('\n\n\n########## line 21 ##########\n')
a = 1
print(f'a={a}, it\'s a {type(a)}')
a = 1.5
print(f'now a={a}, it\'s a {type(a)}')
a = '2'
print(f'and now a={a}, it\'s a {type(a)}')

print('1\n2\n3\n4')


# wait for enter, ignore the content
input();print('\n\n########## line 33 ##########')
print(f'True is a {type(True)}')
print(f'False is also a {type(False)}')

print('if condition is True, the code inside the block will be executed')
if True:
    print('HI~~~')

print('if condition is False, the code inside the block will NOT be executed')
if False:
    print('should not print this line')

input();print('\n')

x = 0
print(f'x == 0 is {x == 0}')
print(f'x > 0 is {x > 0}')
print(f'x < 0 is {x < 0}')
print(f'x >= 0 is {x >= 0}')


input();print('\n\n')


print('How about `if \'hi\':` ?')
if 'hi':
    print('\'hi\' is True. \n Why?')
    print('because python has Truthy and Falsy.')
    print(f'In `if xxx:`, xxx will be either True or False, because `if xxx:` is actually `if bool(xxx):`.')
    print(f'you may consider `bool()` as a function which always returns a {type(True)}')
    print(f'Therefore, no matter what type xxx is, it\'ll always become a {type(True)}')
    print()
    print(f'bool(1) is {bool(1)}')
    print(f'bool(-1) is {bool(-1)}')
    print(f'bool(0) is {bool(0)}')
    print(f'''bool('') is {bool('')}''')
    print(f'''bool('blah') is {bool('blah')}''')
    print(f'bool(None) is {bool(None)}')
    print(f'bool(True) is {bool(True)}')
    print(f'bool(bool(bool(True))) is {bool(bool(bool(True)))}')
    print(f'bool(not True) is {bool(not True)}')
    print(f'bool(not False) is {bool(not False)}')


input();print('\n\n')


b = 1 == 1
print(f'b = 1 == 1, 1 == 1 is {1 == 1} so b is {b}')
if b:
    print('HI~~~')

c = 0
print(f'c = 0 and bool(c) is {bool(c)}')
if c:
    print('so this line won\'t be printed')

if not c:
    print(f'not c means `not bool(c)` and that\'s {not bool(c)} ')
