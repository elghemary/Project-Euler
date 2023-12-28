sumSqr = 0
SqrSum = 0
Sum = 0
diff = 0
count = 1
num = 1

while num < 101:
    sumSqr += num**2
    Sum += num
    num += 1
    count += 1

SqrSum = Sum **2
diff = SqrSum - sumSqr
print (diff)
