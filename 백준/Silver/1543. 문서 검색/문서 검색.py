import sys
input = sys.stdin.readline

string = input().rstrip()
keyword = input().rstrip()

print(string.count(keyword))