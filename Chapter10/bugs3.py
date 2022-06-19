# Me Computer, Mandalay.
# Oct 12, 2017
# bugs3.py
# debugging and search

from re import A


def isPal(x):
    assert type(x) == list
    temp = x
    # temp = x[:]             # fixing by cloning
    print(temp, x)          # next testing
    temp.reverse()          # fixing another bug, but exist aliasing bug
    print(temp, x)          # another testing
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []             # fixed
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
        #print(result)       # testing
    if isPal(result):
        print('Yes')
    else:
        print('No')

# silly(5)