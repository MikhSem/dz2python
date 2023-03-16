import random

n = int(input("Введите количество монеток: "))
coins = [random.choice([1, 0]) for _ in range(n)]

count_heads = sum(coins)
count_tails = n - count_heads

min_flips = min(count_heads, count_tails)

print(f"Список монеток (1 - орёл, 0 - решка): {coins}\nКоличество орлов (1): {count_heads}\nКоличество решек (0): {count_tails}")
print("Минимальное количество переворотов: ", min_flips)




S = int(input("Введите сумму чисел (S): "))
P = int(input("Введите произведение чисел (P): "))

if P > 1000000:
    print("Произведение чисел слишком велико. Пожалуйста, введите другие значения.")
else:
    for Y in range(1, S):
        X = S - Y
        if X * Y == P:
            print(f"Значения X и Y: {X} и {Y}")
            break
    else:
        print("Условие задачи не может быть выполнено с заданными значениями S и P. Пожалуйста, введите другие значения.")
