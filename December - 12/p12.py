input=[3,1,2,2,5]
n=5

repeated=0
missing=0

for num in input:
  val=abs(num)

  if input[val-1]>0:
    input[val-1]=-input[val-1]
  else:
    repeated=val

for i in range(n):
   if input[i]>0:
     missing=i+1

print(f"Repeated number: {repeated}\nMissing number: {missing}")
