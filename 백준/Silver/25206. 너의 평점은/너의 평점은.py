grade_chart = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score_chart = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total_score = 0
credit = 0
for _ in range(20):
    a = input().split()
    if a[2] != 'P':
        total_score += score_chart[grade_chart.index(a[2])] * float(a[1])
        credit += float(a[1])
if credit != 0:
    print(f'{total_score/credit:.6f}')
else:
    print(f'{0:.6f}')