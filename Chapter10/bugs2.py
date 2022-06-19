# Me Computer, Mandalay.
# Oct 12, 2017
# bugs2.py
# debugging and search

def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []             # debugging
    for i in range(n):
        # result = []
        elem = input('Enter element: ')
        result.append(elem)
        print(result)        # testing
    print(result)           # testing
    if isPal(result):
        print('Yes')
    else:
        print('No')

# silly(5)