import random

target_number = random.randint(1, 100)

attempts = 0

while True:
    user_guess = int(input("Попробуйте угадать число от 1 до 100: "))
    attempts += 1
    
    if user_guess < target_number:
        print("Загаданное число больше. Попробуйте еще раз.")
    elif user_guess > target_number:
        print("Загаданное число меньше. Попробуйте еще раз.")
    else:
        print(f"Поздравляю! Вы угадали число {target_number} за {attempts} попыток.")
        break
