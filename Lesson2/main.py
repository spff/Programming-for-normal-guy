a = []
print(f'a is {a}. it\'s a {type(a)}, it\'s empty, so it\'s length is {len(a)}')
print('append 5 to a')
a.append(5)
print(f'now a is {a}, it\'s length is {len(a)}')
print('append 10 to a')
a.append(10)
print(f'now a is {a}, it\'s length is {len(a)}')
print('append 15 to a')
a.append(15)
print(f'now a is {a}, it\'s length is {len(a)}')
print()
print(f'the first element of a is {a[0]}')
print(f'the second element of a is {a[1]}')
print(f'the third element of a is {a[2]}')
print(f'the last element of a is {a[-1]}')
print()
print('assign \'hi\' to the second element of a')
a[1] = 'hi'
print(f'a is now {a}, and you\'ll find that those elements don\'t need to be the same type')

input('\n########## line 22 ##########\n')

print(f'the full sublist of a is {a[:]}')
print(f'a[0:1] is {a[0:1]}')
print(f'a[0:] is {a[0:]}')
print(f'a[:2] is {a[:2]}')
print(f'a[1:2] is {a[1:2]}')

input('\n########## line 30 ##########\n')

b = [7,8,9]
print(f'we concat a & b by a+b, a+b is {a+b}')
print(f'and b+a is {b+a}')


c = b
print(f'after `c=b`, c is now {c}')
c.append(10)
print(f'c is now {c}')
print(f'and b also becomes to {b}')
print('that\'s because both b & c are referencing to the same `list`')
c = [2,2,2]
print(f'we ASSIGN another list to c, so c is now {c}, and b is still {b}')


input('\n########## line 47 ##########\n')

print('BTW, what the a[0:1] do is constructing a new list [], and append all elements in the range from the original list')
c = b[0:1]
print(f'b={b}, c={c}')
c.append(6)
print(f'b={b}, c={c}, this won\'t affect b because b and c are referencing to different lists, that means they are independent.')


print()
print('''
here, => means 'reference to', or 'point to'

a = [0,1,2]
# 1. [0,1,2]
# 2. a => [0,1,2]

b = a
# 3. a \\
#        =>[0,1,2]
#    b /

c = a[:]
# 4. a \\
#       =>[0,1,2]
#    b /
#    [0,1,2]
#
# 5. a \\
#       =>[0,1,2]
#    b /
#    c => [0,1,2]

''')

input('\n########## line 82 ##########\n')

a = 1
b = 2
# assign 3 to c
c = 3
# if a equals to 1
if a == 1:
    print('a == 1 is True')
elif b == 2:
    print('b == 2 is True')
else:
    print('else')

if a == 1 and (b == 2 or c != 0):
    if c == 2:
        print('c==2')
    elif c == 3:
        print('c == 3')
else:
    print('a != 1 or (b != 2 and c == 0)')

a = 0
while a < 5:
    a += 1
    print(f'a = {a}')
print()

b = 0
while b <= 5:
    b += 2
    print(f'b = {b}')
else:
    print(f'else, b = {b}')

input_len = -1
while input_len != 0:
    s = input('type something to loop or just press ENTER to leave')
    input_len = len(s)
    print(f'you typed {s}, input_len={input_len}')

while 'abc' not in input('type something'):
    print(f'your input doesn\'t contains \'abc\'')


input('\n########## line 127 ##########\n')

the_list = [5,4,3]
for element in the_list:
    print(f'element is {element}')
else:
    print('end of for')
print()

the_doubled_list = [ element*2 for element in the_list]
print(f'the_doubled_list={the_doubled_list}')
print()

for doubled_element in the_doubled_list:
    print(f'doubled_element is {doubled_element}')
print()

# we can do some filtering
the_even_list = [ element for element in the_list if element%2 == 0]
print(f'the_even_list={the_even_list}')


print(f'sorted_list={sorted(the_list)}')
for sorted_element in sorted(the_list):
    print(f'sorted_element is {sorted_element}')
print()

for sorted_element_from_second in sorted(the_list)[1:]:
    print(f'sorted_element_from_second is {sorted_element_from_second}')
print()


# Not only list can be iterated with for, you'll see more in the following lessons.
for char in 'aoeu':
    print(f'char={char}')



input('\n########## line 165 ##########\n')

# Define a function called dummy which takes 1 argument and straightly return it.
def dummy(x):
    return x

print(f'{dummy(100)}, {dummy([3, "4"])}, {dummy(None)}')

# Define a function called return_first which takes 2 arguments and return None
def return_first(x, y):
    print(f'x={x}, y={y}')
    return x

def return_none_1():
    return None

def return_none_2():
    return

def return_none_3():
    print('hi')

print(f'{return_first(5, 6)}, {return_none_1()}, {return_none_2()}, {return_none_3()}')

# you can assign default value
def custom_add(a, b=5):
    return a+b

print(f'{custom_add(3)}, {custom_add(3,5)}, {custom_add(3,6)}')

input('\n########## line 195 ##########\n')

def gen_list_135():
    return [1,3,5]

print(f'the return of gen_list_135 is {gen_list_135()}')

def fibonacci_list(count):
    ret = [0,1]
    while len(ret) < count:
        ret.append(ret[-2]+ret[-1])
    return ret[:count]

print()
for element in fibonacci_list(10):
    print(f'element is {element}')

print('''
sometimes, we want to generate the element dynamically instead of preparing the full list & iterating.

for several reasons
1. we're not sure how long the list should be
2. the list might be very huge, and we only care about the current element (not going to reuse the previous ones)

so here we have `generator` to acheive this, and the only limitation is you can only iterate it once, forward, and you cannot index it
''')

# we import a standard library (the opposite of standard library is a third party library)
import time
def slow_fibonacci_list(count):
    ret = [0,1]
    while len(ret) < count:
        time.sleep(0.4)
        n = ret[-2]+ret[-1]
        print(f'append {n}', flush=True)
        ret.append(n)
    return ret[:count]

print('''
we want to print all fibonaccis less than or equal to 10 by using slow_fibonacci_list, which takes a count,
and we guess the 20th element might be greater than 10
''', flush=True)
fl = slow_fibonacci_list(20)
print(f'fl={fl}, it\'s a {type(fl)}')
for element in fl:
    if element > 10:
        # leave the for loop
        break
    print(f'element is {element}')

print('\na better approach would be using generator, which also takes `count` as an input but you can terminate it and generate elements dynamiccaly')
def slow_fibonacci_gen(count):
    a = 0
    b = 1
    c = 0
    yield 0
    yield 1
    while c < count:
        time.sleep(0.4)
        n = a + b
        print(f'the next is {n}', flush=True)
        a = b
        b = n
        # the return will leave the function and return the value(default is None)
        # the yield will return the value and wait, and might keep running when needed
        yield n

fg = slow_fibonacci_gen(200)
print(f'fg={fg}, it\'s a {type(fg)}', flush=True)
for element in fg:
    if element > 10:
        # leave the for loop
        break
    print(f'element is {element}')

print('see~ you don\'t need to wait for all of the 200 elements been calculated')

input('\n########## line 270 ##########\n')

r1 = range(10)
r2 = range(2, 10)
r3 = range(2, 10, 3)
r4 = range(10, -5, -2)
print(f'{r1} {r2} {r3} {r4}')
for x in r1:
    print(x)

print('you may put all elements from generator into a list')
print(f'{[x for x in r1]}')
print('you may also directly construct a list by calling `list()`, and put the generator as the arguement')
print(f'list(r1)={list(r1)}')
print(f'list(r2)={list(r2)}')
print(f'list(r3)={list(r3)}')
print(f'list(r4)={list(r4)}')

#import another standard library : pathlib
import pathlib
# list all files in the same directory of this python file with their first line 
g = pathlib.Path(__file__).parent.iterdir()
print(f'g={g}')
for child in g:
    if child.is_file():
        firstline = child.read_text(errors='ignore').split('\n')[0]
        print(f'first line of {child.resolve()} is {firstline}')
