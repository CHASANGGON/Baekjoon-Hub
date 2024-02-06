def common_divisor(a,b):
    if b == 0:
        return a
    else:
        return common_divisor(b,a%b)

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
c,d = map(int,input().split())
    
a,b,c = a*d,b*d,c*b

son,mom = a+c,b # 분자, 분모

if mom > son:
    cm_dvs = common_divisor(mom,son)
else:
    cm_dvs = common_divisor(son,mom)
print(son//cm_dvs, mom//cm_dvs)