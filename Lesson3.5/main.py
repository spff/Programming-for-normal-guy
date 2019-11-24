for a, b, c in [(1,2,3), (4,5,6), (7,8,9)]:
    print(a,b,c)
print()
print(list(enumerate([6,7,8])))
print()
for index, element in enumerate([6,7,8]):
    print(index, element)
print()

for left, right in zip(['a', 'b', 'c'], range(7,10)):
    print(left, right)