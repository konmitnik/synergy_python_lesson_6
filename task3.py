a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
even_nums = []

for i in range(a, b + 1):
    if i % 2 == 0:
        even_nums.append(str(i))

print(f"Четные числа на отрезке {a} - {b}: {' '.join(even_nums)}")