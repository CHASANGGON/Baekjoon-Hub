n = int(input())

dic = {}
age_lst = []
for _ in range(n): # 나이별로 딕셔너리에 추가
    age, name = input().split()
    age = int(age)
    age_lst.append(age)
    if age not in dic:
        dic[age] = [name]
    else:
        dic[age] += [name]


age_lst = list(set(age_lst)) # 출력을 위해 age_lst set처리
age_lst.sort() # age 오름차순

for a in age_lst: # 출력
    for name in dic[a]:
        print(a, name)