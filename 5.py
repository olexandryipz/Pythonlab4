from random import randint

numbers = [randint(-100, 100) for _ in range(30)]
print("Список:", numbers)

negative_pairs = [(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1) if numbers[i] < 0 and numbers[i+1] < 0]

if negative_pairs:
    print("Пари від'ємних чисел, що стоять поруч:", negative_pairs)
else:
    print("Пар від'ємних чисел, що стоять поруч, немає.")