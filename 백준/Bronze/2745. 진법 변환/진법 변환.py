number, b = input().split()
b = int(b)

sum = 0
length = len(number) - 1
for n in number:
    if  b >= 10:
        if n in "0123456789":
            n = int(n)     
            sum += n * b ** length
        else:
            sum += (ord(n) - 55 ) * b ** length
    else :
        sum += int(n) * b ** length
    length -= 1
print(sum)