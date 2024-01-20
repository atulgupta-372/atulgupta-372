def lengCac(x,a):
  low,high=0,0
  if x[1]>=a[0] :
    if x[0]>=a[1]:
      return 0
    else:
      high=min([x[1],a[1]])
      low=max([x[0],a[0]])
  return high-low

def OverlappingRectangles(strArr):
  arr=[]
  flag=False
  for i in strArr[0]:
    if i=="-":
      flag=True
    if i.isdigit():
      if flag==True:
        arr.append(int(i)*-1)
        flag=False
      else:
        arr.append(int(i))

  x1,y1,x2,y2,x3,y3,x4,y4=[i for i in arr[:8]]
  xArr=set([x1,x2,x3,x4])
  yArr=set([y1,y2,y3,y4])

  a1,b1,a2,b2,a3,b3,a4,b4=[i for i in arr[8:]]
  aArr=set([a1,a2,a3,a4])
  bArr=set([b1,b2,b3,b4])
  #print(xArr,yArr,aArr,bArr)
  #Area1=abs((xArr[0]-xArr[1])*(yArr[1]-yArr[0]))
  length,breath=0,0

  xArr=sorted(xArr)
  yArr=sorted(yArr)
  aArr=sorted(aArr)
  bArr=sorted(bArr)
  Area1=abs((xArr[0]-xArr[1])*(yArr[1]-yArr[0]))

  #print(xArr,yArr,aArr,bArr,Area1)

  length=lengCac(xArr,aArr)
  breath=lengCac(yArr,bArr)

  lapArea=length*breath
  if lapArea==0:
    return 0
  else:
    return int(Area1/lapArea)


# keep this function call here 
print(OverlappingRectangles(input()))