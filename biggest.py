a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= b and a >= c:
    big = a
elif b >= a and b >= c:
    big = b
else:
    big = c

print(f"Наибольшее из введенных чисел: {big}")
