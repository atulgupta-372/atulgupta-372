def median(arr):
  if len(arr)%2!=0:
    return arr[int(len(arr)/2)]
  else:
    return int((arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)])/2)

def push(arr,x):
  flag=False
  i=0
  for i in range(len(arr)):
    if arr[i]>=x:
      flag=True
      break
  if flag==True:
    arr.insert(i,x)
  else:
    arr.insert(i+1,x)
  return arr

def MovingMedian(arr):
  arr1=[]
  arr2=[]
  size=arr.pop(0)
  #print(size)
  #push(arr,5)
  for i in range(0,size):
    if len(arr)==0:
      break
    pre=arr.pop(0)
    push(arr2,pre)
    arr1.append(median(arr2))

  while len(arr)>0:
    arr2.remove(pre)
    pre=arr.pop(0)
    arr2=push(arr2,pre)
    arr1.append(median(arr2))

  return arr1

# keep this function call here 
print(MovingMedian(input()))