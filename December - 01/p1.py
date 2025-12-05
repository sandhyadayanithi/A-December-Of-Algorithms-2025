import math

def perfectSqCounter(n):
    count=0
    for i in range (1,n):
        sq=math.sqrt(i)
        if sq.is_integer():
            print(f'{i }',end=" ")
            count+=1
    return count

count=perfectSqCounter(20)
print()
print(count)
