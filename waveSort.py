def WaveSorting(arr):
  arr.sort()
  arr1=arr[:int(len(arr)/2)]
  arr2=arr[:int(len(arr)/2)-1:-1]
  arr2=arr2[::-1]
  #print(arr1,arr2[::-1],arr2)

  if len(arr2)==len(arr1):
    for i in range(len(arr1)):
      if arr1[i]>=arr2[i]:
        return "false"
  else:
    for i in range(len(arr1)):
      if arr1[i]>=arr2[i]:
        return "false"
    if arr2[-1]>arr1[-1]:
      return "true"
    else:
      return "false"
  return "true"
# keep this function call here 
print(WaveSorting(input()))