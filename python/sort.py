from search import Max

def insert(n):
    for j in range(1, len(n)):
        x=Max(n[0:j],n[j],0,j-1)
        if x is None:
            x=j
        y=n[j]
        del n[j]
        n.insert(x,y)
    return n

def max_sort(n):
    def max_index(n, last):
        macs=-1
        number=-1
        for i in range(last):
            if(n[i]>macs):
                macs=n[i]
                number=i
        return number
    
    x=len(n)-1
    while(x!=-1):
        ind = max_index(n, x+1)
        n[ind], n[x] = n[x], n[ind]
        x=x-1
    return n

def bubble(n):
    x=len(n)
    count=0
    while(x!=0):
        for i in range(x-1):
            if(n[i]>=n[i+1]):
                y=n[i]
                n[i]=n[i+1]
                n[i+1]=y
                count=count +1
        x=x-1
    #print(count)
    return n
