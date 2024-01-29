data = list(input())

for str in data:
    number = ord(str) - 64
    print(f"{number}", end=" ")
