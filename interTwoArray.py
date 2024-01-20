num1= [int(x) for x in input().split()]
num2= [int(x) for x in input().split()]
numhash1=[bool(False) for x in range(100)]
numhash2=[bool(False) for x in range(100)]

answer=[]
for i in num1:
    numhash1[i]=True
for i in num2:
    numhash2[i]=True
for i in range(len(numhash1)):
    if numhash1[i]==numhash2[i]:
        answer.append(i)
print(answer)
        


