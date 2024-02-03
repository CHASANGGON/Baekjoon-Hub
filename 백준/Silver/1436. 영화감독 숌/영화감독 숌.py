import sys
N = int(sys.stdin.readline())
end_of_day = 0

while N > 0 :
    if '666' in str(end_of_day):
        N -= 1
        end_of_day += 1
    else:
        end_of_day += 1
print(end_of_day-1)