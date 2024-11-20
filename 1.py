try:
    numbers = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))
    if not numbers:
        raise ValueError("Список не може бути порожнім")
except ValueError as e:
    print(f"Помилка введення: {e}")
else:
    max_element = max(numbers)
    print(f"Максимальний елемент: {max_element}")

    reversed_list = numbers[::-1]
    print("Список у зворотному порядку:", reversed_list)