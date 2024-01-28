import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    sum = 0
    data = list(map(int, input().split()))
    for number in data:
        sum = sum + number
    avg = round(sum/10)
    print(f"#{i+1} {avg}")
