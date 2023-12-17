def can_construct(s1, s2):
    # Преобразуем строки в множества уникальных символов
    set_s1 = set(s1)
    set_s2 = set(s2)

    # Проверяем, содержит ли множество символов s1 все символы из s2
    return set_s1.issubset(set_s2)


s1 = "hello"
s2 = "world"
print(can_construct(s1, s2))  # Выведет False

s1 = "hello"
s2 = "helloworld"
print(can_construct(s1, s2))  # Выведет True
