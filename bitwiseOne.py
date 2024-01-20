def BitwiseOne(strArr):
  string=""
  for i in range(len(strArr[0])):
    if strArr[0][i]=="0" and strArr[1][i]=="0":
      string+="0"
    else:
      string+="1"
  return string

# keep this function call here 
print(BitwiseOne(input()))