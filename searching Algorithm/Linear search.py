def linearsearch(a,e1):
  ar=[]
  for i in range(len(a)):
    if a[i]==e1:
      
       ar.append(i)
  
  if len(ar)>0:
    return ar
  return -1
a=[12,3,14,22,56,75,14]
print(linearsearch(a,15))
