import sys

my_cards = [0]*20000001

sys.stdin.readline()
idx = list(map(int,sys.stdin.readline().split()))

for i in idx:
    my_cards[i+10000000] += 1

m = int(sys.stdin.readline())
your_cards = list(map(int,sys.stdin.readline().split()))

for card in your_cards:
    print(my_cards[card+10000000],end=' ')