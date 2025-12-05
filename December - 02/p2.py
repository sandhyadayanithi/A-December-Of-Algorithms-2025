def binary(n):
  if n==0:
    return [0]
  bList=[]
  while n>0:
    bList.append(n%2)
    n=n//2

  bList.reverse()
  return "".join(map(str,bList))

def octal(n):
  if n==0:
    return [0]
  oList=[]
  while n>0:
    oList.append(n%8)
    n=n//8

  oList.reverse()
  return "".join(map(str,oList))

hexConversion={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def hexa(n):
  if n==0:
    return [0]
  hList=[]
  while n>0:
    hList.append(n%16)
    n=n//16

  for i in range (len(hList)):
    if hList[i] in hexConversion:
      hList[i]=hexConversion[hList[i]]

  hList.reverse()
  return "".join(map(str,hList))

n=5
for i in range(1,n+1):
  print(f'{i, i, (octal(i)), (hexa(i)), (binary(i))}')
  print()