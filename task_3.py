#3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input("Введите число:  "))
ls = list()
sum_elem = 0
for i in range(1, n+1):
    ls.append(round((1 + 1 / i) ** i))
    sum_elem = sum(ls)

print(f"Для n = {n}: {ls} сумма равна {sum_elem}")


