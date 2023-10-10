num = int(input("Введите число: "))

for lp in range(num):
    if lp == num:
        break
    if lp < num:
        print(f"{lp}")
    else:
        print(f"{lp}")