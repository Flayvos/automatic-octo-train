n = count = count2 = 0
while True:
    n += 1
    for c in range(1, n + 1):
        if n % c == 0:
            count2 += 1
    if count2 == 2:
        count += 1
        print(f'\33[41m\33[33m|\33[33m{n}\33[33m|', end = '\33[33m → ')
        if count == 20:
            print('\n', end = '')
            count = 0
    count2 = 0
