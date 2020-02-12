from random import randrange
from copy import copy

from sort import insert, max_sort, bubble

N_MAX = 1000

def compare(method, arr):
    arr1 = copy(arr)
    arr2 = copy(arr)

    try:
        method(arr1)
    except:
        print("Exception:", arr)
        return
    arr2.sort()
    if (arr1 == arr2):
        print("OK")
        #pass
    else:
        print("Different answers:", arr, arr1, arr2)

if __name__ == "__main__":
    for i in range(300):
        length = randrange(1, 100)
        arr = []
        for j in range(length):
            arr.append(randrange(0, N_MAX))
        compare(bubble, arr)


#res = insert([535, 787, 927])
#print(res)
