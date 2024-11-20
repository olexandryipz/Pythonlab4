from random import uniform

numbers = [uniform(-100, 100) for _ in range(30)]
print("Список:", numbers)

min_abs_element = min(numbers, key=abs)
print("Мінімальний по модулю елемент:", min_abs_element)

numbers.sort()
print("Список у порядку зростання:", numbers)