from random import randint

numbers = [randint(-100, 100) for _ in range(20)]
print("Список:", numbers)

sum_odd_indices = sum(numbers[i] for i in range(1, len(numbers), 2))
print("Сума елементів з непарними індексами:", sum_odd_indices)