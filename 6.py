try:
    numbers = list(map(int, input("Введіть список з 10 цілих чисел через пробіл: ").split()))
    if len(numbers) != 10:
        raise ValueError("Список повинен містити рівно 10 елементів")
except ValueError as e:
    print(f"Помилка введення: {e}")
else:
    max_element = max(numbers)
    smaller_squares = [num**2 for num in numbers if num < max_element]
    smaller_squares.sort(reverse=True)

    print(f"Максимальний елемент: {max_element}")
    print("Квадрати менших чисел (у порядку спадання):", smaller_squares)
