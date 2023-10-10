num = int(input("Введите число: "))

divisors = []

for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

print(f"Делители числа {num}: {divisors}")