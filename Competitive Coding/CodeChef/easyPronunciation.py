num=int(input())
for i in range(num):
    length=int(input())
    str1=input()
    maxi=0
    count=0
    for j in str1:
        if j in "aeiou":
            count=0
        else:
            count+=1
        if count>maxi:
            maxi=count
    if maxi>=4:
        print("NO")
    else:
        print("YES")
