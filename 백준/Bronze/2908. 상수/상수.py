num1, num2 = input().split()

reverse_num1 = ''
for num in num1:
    reverse_num1 = num + reverse_num1

reverse_num2 = ''
for num in num2:
    reverse_num2 = num + reverse_num2

if int(reverse_num1) > int(reverse_num2):
    print(reverse_num1)
else:
    print(reverse_num2)