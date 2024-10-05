total = 0
count = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        count += 1
        total += n
print(f'A soma de todos os {count} valores solicitados e {total}')
