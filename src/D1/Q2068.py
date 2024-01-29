T = int(input())

for i in range(T):
    data = list(map(int, input().split()))
    max_value = -1
    for number in data:
        if max_value < number:
            max_value = number
    print(f"#{i+1} {max_value}")
