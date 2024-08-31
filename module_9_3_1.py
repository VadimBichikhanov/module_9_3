first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Первая генераторная сборка
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Вторая генераторная сборка
second_result = map(lambda i: len(first[i]) == len(second[i]), range(min(len(first), len(second))))
# Вывод результатов
print(list(first_result))
print(list(second_result))
