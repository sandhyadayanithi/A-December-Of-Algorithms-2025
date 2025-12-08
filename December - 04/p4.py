def subArray(input,n,target):
  sum=0
  start,end=0,0
  found=0
  for i in range(n):
    if sum<target:
      sum+=input[i]
      end=i
    while sum>target:
      sum-=input[start]
      start+=1
    if sum==target:
      found=1

  if found:
    print(f'{start, end}')
  else:
    print((-1, -1))

n=7
target=15
input=[1,2,3,7,5,1,2]

subArray(input,n,target)