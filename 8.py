from random import uniform

numbers = [uniform(-100, 100) for _ in range(30)]
print("Список:", numbers)

sub_lists = [numbers[i:i+3] for i in range(0, 30, 3)]

sorted_sub_lists = sorted(sub_lists, key=lambda lst: sum(abs(x) for x in lst))

print("Підсписки у порядку зростання за сумою абсолютних значень:")
for sublist in sorted_sub_lists:
    print(sublist)