input()
lst_n = set(map(int,input().split()))
# set에서 다시 list로 만드니 탐색시간이 엄청 길어짐
# set를 쓰면 순서가 없어서 인덱스 접근은 못 하지만
# 멤버십 연산자는 상관없이 쓸 수 있다!!
# 문제의 의도는 이분 탐색이라고 한다..
input()
lst_m = list(map(int,input().split()))

for m in lst_m:
    if m in lst_n:
        print(1)
    else:
        print(0)