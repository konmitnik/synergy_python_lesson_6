n = int(input('Введите число N: '))
lst = list()

for i in range(n):
    lst.append(int(input('Введите свое целое число: ')))

print(f"Вы ввели число 0 - {lst.count(0)} раз")