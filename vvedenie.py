# 1st program
result = 9 ** 0.5 * 5
print(result)  # Ожидаемый результат: 15.0

# 2nd program
result = 9.99 > 9.98 and 1000 != 1000.1
print(result)  # Ожидаемый результат: True

# 3rd program
without_priority = 2 * 2 + 2  # 2 умноженное на 2 плюс 2 без приоритета (4 + 2)
with_priority = 2 * (2 + 2)  # 2 умноженное на (2 плюс 2) с приоритетом для сложения (2 * 4)
comparison = without_priority == with_priority
print(without_priority)  # Ожидаемый результат: 6
print(with_priority)  # Ожидаемый результат: 8
print(comparison)  # Ожидаемый результат: False

# 4th program
number = '123.456'
float_number = float(number)  # Преобразуем строку в дробное число
shifted = float_number * 10  # Смещаем первую цифру после точки в целую часть (1234.56)
first_digit_after_dot = int(shifted) % 10  # Извлекаем первую цифру после запятой
print(first_digit_after_dot)  # Ожидаемый результат: 4
