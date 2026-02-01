
def qs(zahlen:list):
    qsL=[]
    qsR=[]
    if len(zahlen) <= 1:
        return zahlen
    
    print(zahlen)
    privot = zahlen[len(zahlen)-1]
    for i in zahlen:
        if i < privot:
            qsL.append(i)
        elif i>privot:
            qsR.append(i)  

    return qs(qsL)+[privot]+qs(qsR)
    
print(*qs([10,5,8,14,6,22,48,7,1]))