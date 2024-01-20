def PowersofTwo(num):
  num=int(num)
  if num>0 and num&(num-1)==0:
    return "true"
  return "false"

# keep this function call here 
print(PowersofTwo(input()))