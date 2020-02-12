def Max2(n,k):
    for i in range(len(n)):
        if(n[i]>=k):
            return i
    return None

def Max(n,k,first,last):
    if n[0] >= k:
        return 0
    if(n[len(n)-1]<k):
        return None
    else:
        if((last-first)<=1):
            if(n[first]>=k):
                return first
            else:
                return last
        else:
            if(n[(last+first)//2]>=k):
                return Max(n,k,first,(last+first)//2)
            if(n[(last+first)//2]<k):
                return Max(n,k,first+((last-first)//2),last)
