sum = 0
F1 = 1
F2 = 2
F3 = 3

while F2 < 4000000:
    if F2 % 2 == 0 :
        sum += F2
    F1 = F2
    F2 = F3
    F3 = F1 + F2
print (sum)
