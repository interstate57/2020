from search import Max, Max2
from random import randrange

N_MAX = 10000

def compare(arr, k):
    try:
        res1 = Max(arr, k, 0, len(arr) - 1)
    except:
        print("Exception:", arr, k)
        return
    res2 = Max2(arr, k)
    if (res1 == res2):
        print("OK")
        pass
    else:
        print("Different answers:", arr, k, res1, res2)


#compare([4,5,6,12,15,32], 1)

if __name__ == "__main__":

    for i in range(100000):
        print(i)
        length = randrange(1, 100)
        arr = []
        for j in range(length):
            arr.append(randrange(0, N_MAX))
        arr.sort()
        compare(arr, randrange(0, N_MAX + 1000))
