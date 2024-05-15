x = int(input('Введите натуральное число X: '))
count_denominators = 0

for i in range(1, x + 1):
    if x % i == 0:
        count_denominators += 1

print(f"Количество натуральных делителей Вашего числа: {count_denominators}")