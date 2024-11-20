try:
    numbers = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))
    if not numbers:
        raise ValueError("Список не може бути порожнім")
except ValueError as e:
    print(f"Помилка введення: {e}")
else:
    positive_numbers = [num for num in numbers if num > 0]
    negative_numbers = [num for num in numbers if num <= 0]

    print("Додатні числа:", positive_numbers)
    print("Від'ємні та нульові числа:", negative_numbers)