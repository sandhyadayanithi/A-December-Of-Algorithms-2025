import math

n=20

isPrime = [0, 0] + [1]*(n-2)

for i in range(2,n):
  if isPrime[i]==1 and i<=math.sqrt(n):
    for j in range(i**2,n,i):
      isPrime[j]=0

count=0
for i in range(2,n):
  if isPrime[i]==1:
    count+=1

print(count)

# Time complexity: O(nlog(logn))