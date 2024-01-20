def HistogramArea(arr):
  arr=list(map(int,arr))
  #arr=eval(arr)
  arr1=arr.copy()
  maxArea=0
  arrArea=[]
  min1=arr[0]
  l=len(arr)
  while arr:
    min1=min(arr)
    min2=min(arr1)
    arrArea.append(l*min1)
    arrArea.append(l*min2)
    arr.pop(0)
    arr1.pop()
    l-=1
  maxArea=max(arrArea)
  return maxArea

# keep this function call here 
print(HistogramArea(input()))