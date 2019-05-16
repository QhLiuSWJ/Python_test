##
test=['a','b','c']
ifornot='a' in test
print(str(ifornot))

if 'a' in test:
    test.append('d')
    print(test)
if 'b' not in test:
    print('b')
elif 'a' not in test:
    print('c')
else:
    print('d')
