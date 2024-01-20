def ScaleBalancing(strArr):
  num=""
  for x in strArr[0]:
    if ord(x)>=48 and ord(x)<59:
      num+=x
    elif x==",":
      left=int(num)
      num=""
  right=num
  print(left,right)
  num=""
  numlist=[]
  for x in strArr[1]:
    if ord(x)>=48 and ord(x)<59:
      num+=x
    elif x==",":
      numlist.append(int(num))
      num=""
  numlist.append(int(num))
  print(numlist)
    

  return strArr

# keep this function call here 
print(ScaleBalancing(input()))