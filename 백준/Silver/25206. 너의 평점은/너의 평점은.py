total_grade = 0
credit = 0
for _ in range(20):
    a, b, c = input().split()
    if c != 'P':
        credit += float(b)
        if c == 'A+':
            grade = 4.5
        elif c == 'A0':
            grade = 4.0
        elif c == 'B+':
            grade = 3.5
        elif c == 'B0':
            grade = 3.0
        elif c == 'C+':
            grade = 2.5
        elif c == 'C0':
            grade = 2.0
        elif c == 'D+':
            grade = 1.5
        elif c == 'D0':
            grade = 1.0
        else:
            grade = 0
        total_grade += float(b)*grade
        
if credit != 0:
    print(f'{total_grade/credit:.6f}')
else:
    print(f'{0:.6f}')
