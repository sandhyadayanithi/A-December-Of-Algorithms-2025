ops = ["5","2","C","D","+"]
record=[]

for s in ops:
  if s=='+':
      sum=int(record[-1])+int(record[-2])
      record.append(sum)
  elif s=='D':
      sum=int(record[-1])*2
      record.append(sum)
  elif s=='C':
      record.pop()
  else:
      record.append(int(s))

res=0
for r in record:
  res+=r

print(res)