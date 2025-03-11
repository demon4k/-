class Dmytro:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_course(self):
        if self.birth_year:
            current_year = 2025  # Припустимо, що зараз 2025 рік
            age_at_start = 15  # Вік вступу до університету
            return max(1, current_year - self.birth_year - age_at_start)
        return None

    def get_name_list(self):
        return [self.name, self.surname]


# Введення даних з консолі
name = input("Введіть ім'я: ")
surname = input("Введіть прізвище: ")

# Перетворюємо введений рік народження в число (int)
while True:
    try:
        birth_year = int(input("Введіть рік народження: "))
        break  # Вийти з циклу, якщо введено правильне число
    except ValueError:
        print("Будь ласка, введіть коректний рік народження (число).")

# Створення об'єкта
student = Dmytro(name, surname, birth_year)

print(f"Ім'я: {student.name}")
print(f"Прізвище: {student.surname}")
print(f"Рік народження: {student.birth_year}")
print(f"Курс: {student.get_course()}")
print(f"Список (Ім'я, Прізвище): {student.get_name_list()}")






















# class Dmytro:
#     def __init__(self, name=None, surname=None, birth_year=None):
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year

#     def get_course(self):
#         if self.birth_year:
#             current_year = 2025  # Припустимо, що зараз 2025 рік
#             age_at_start = 17  # Вік вступу до університету
#             return max(1, current_year - self.birth_year - age_at_start)
#         return None  # Якщо рік народження не задано

#     def get_name_list(self):
#         return [self.name, self.surname]

# # Приклад використання
# student = Oleksandr("Олександр", "Іваненко", 2004)
# print(student.get_course())  # Виведе курс студента
# print(student.get_name_list())  # Виведе ['Олександр', 'Іваненко']
