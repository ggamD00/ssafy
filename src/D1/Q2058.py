N = int(input())

sum_value = 0
while N > 0:
    sum_value += N % 10
    N = N // 10
print(sum_value)

