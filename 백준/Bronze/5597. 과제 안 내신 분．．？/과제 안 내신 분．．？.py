students = [0]*30

for _ in range(28):
    student = int(input())
    students[student-1] = 1

for i in range(30):
    if students[i] == 0: print(i+1)