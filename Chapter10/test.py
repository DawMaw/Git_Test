# Me Computer, Mandalay.
# Oct 12, 2017
# bugs.py
# debugging and search

def isPal(x):
    assert type(x) == list
    temp = x[:]
    print(temp,x)
    temp.reverse()
    print(temp,x)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result=[]
    for i in range(n):
        # result = []
        elem = input('Enter element: ')
        result.append(elem)
        # print(result)
    # print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')

# silly(2)