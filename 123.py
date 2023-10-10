month = int(input("Введите порядковый номер месяца (1-12): "))
year = int(input("Введите год: "))

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("В этом месяце 31 день.")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("В этом месяце 30 дней.")
elif month == 2:
    if is_leap_year:
        print("В этом месяце 29 дней (високосный год).")
    else:
        print("В этом месяце 28 дней.")
else:
    print("Некорректный номер месяца. Пожалуйста, введите число от 1 до 12.")
