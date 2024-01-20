def ScaleBalancing(strArr):
  leftWeight,rightWeight=eval(strArr[0])    ###eval() takes an expression and gives what will print in Screen###
  weightList=eval(strArr[1])
  for i in weightList:
    if leftWeight+i== rightWeight or rightWeight+i==leftWeight:
      return str(i)
  leftIndex,rightIndex=0,len(weightList)-1
  currentSum=weightList[leftIndex]+weightList[rightIndex]
  while leftIndex<rightIndex:
    if currentSum=abs(rightWeight-leftWeight):
      return str(weightList[leftIndex])+","+str(weightList[rightIndex])
    elif currentSum<abs(rightWeight-leftWeight):
      leftIndex+=1
    else:
      rightIndex-=1
      

  return strArr

print(ScaleBalancing(input()))