T = int(input())

for i in range(T):
    data = input().strip()
    year = data[0:4]
    month = data[4:6]
    day = data[6:8]

    if 1 <= int(month) <= 12:
        if month in ['01', '03', '05', '07', '08', '10', '12']:
            if 1 <= int(day) <= 31:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(f"#{i+1} -1")
        elif month in ['04', '06', '09', '11']:
            if 1 <= int(day) <= 30:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(f"#{i+1} -1")
        elif month == '02':
            if 1 <= int(day) <= 28:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(f"#{i+1} -1")
        else:
            print(f"#{i+1} -1")
    else:
        print(f"#{i+1} -1")
