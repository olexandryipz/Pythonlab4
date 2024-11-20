from random import randint

numbers = [randint(-100, 100) for _ in range(30)]
print("Список:", numbers)

max_element = max(numbers)
max_index = numbers.index(max_element)
print(f"Максимальний елемент: {max_element}, Індекс: {max_index}")

odd_numbers = [num for num in numbers if num % 2 != 0]

if odd_numbers:
    odd_numbers.sort(reverse=True)
    print("Список непарних чисел (у порядку спадання):", odd_numbers)
else:
    print("У списку немає непарних чисел.")