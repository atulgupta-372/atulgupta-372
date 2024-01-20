versions,badVer=map(int,input().split())
operNO=1
high,low=versions,0

i=int(versions/2)
while i!=badVer:
    if i>badVer:
        operNO+=1
        i=int((low+i)/2)
    else:
        operNO+=1
        i=int((i+high)/2)

print(operNO)

