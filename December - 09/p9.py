input=[5,5,5,5,5]
n=5

sum=0
repeated=set()
seen=set()

for i in range(n-1):
  if input[i] in seen:
    repeated.add(input[i])
  else:
    seen.add(input[i])

for num in input:
  if num not in repeated:
    sum+=num

print(sum)