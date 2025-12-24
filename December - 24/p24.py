input="aabbcc"

freq={}
index_array=[]

for c in input:
  freq[c]=freq.get(c,0)+1

found=0
for key,value in freq.items():
  if value==1:
    found=1
    print(f"The first non-repeating character is: {key}")
    break

if found==0:
  print("No non-repeating character found.")
