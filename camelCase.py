def CamelCase(strParam):
  flag=False
  str1=""
  for i in range(len(strParam)):
    if strParam[i].isalpha()==False:
      flag=True
    else:
      if flag==True:
        flag=False
        str1+=strParam[i].upper()
      else:
        str1+=strParam[i].lower()
  return str1

# keep this function call here 
print(CamelCase(input()))