num = int(input("Введите число: "))

divisors_sum = sum([i for i in range(1, num) if num % i == 0])

if divisors_sum == num:
    print(f"{num} - совершенное число.")
else:
    print(f"{num} - не является совершенным числом.")