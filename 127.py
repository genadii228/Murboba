sum_even = 0
sum_odd = 0

while True:
    num = int(input("Введите число (или 0 для завершения): "))
    if num == 0:
        break
    elif num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print(f"Сумма четных чисел: {sum_even}")
print(f"Сумма нечетных чисел: {sum_odd}")
