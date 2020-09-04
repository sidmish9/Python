import math
# https://docs.python.org/3/library/math.html

# if elif


c = True
d = False
print(c or d)

if c:
    if d:
        print('')
    elif c & d:
        print('')
    elif c | d:
        print('caught')

    else:
        print('')
else:
    print('nah')
