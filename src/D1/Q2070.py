T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    inequality = ""
    if N < M: inequality = "<"
    elif N > M: inequality = ">"
    else: inequality = "="
    print(f"#{i+1} {inequality}")