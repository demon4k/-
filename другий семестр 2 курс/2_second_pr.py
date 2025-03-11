class Student:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_course(self):
        if self.birth_year:
            current_year = 2025  # Припустимо, що зараз 2025 рік
            age_at_start = 17  # Вік вступу до університету
            return max(1, current_year - self.birth_year - age_at_start + 1)
        return None

    def get_name_list(self):
        return [self.name, self.surname]


# 🔹 Дочірній клас
class AdvancedStudent(Student):
    def __init__(self, name=None, surname=None, birth_year=None, university=None, faculty=None, average_grade=None):
        # Викликаємо конструктор батьківського класу
        super().__init__(name, surname, birth_year)
        
        # Додаємо 3 нові атрибути
        self._university = university  # Захищений атрибут (protected)
        self.faculty = faculty
        self.__average_grade = average_grade  # Приватний атрибут (private)

    # 🔹 Новий метод 1: Перевіряє, чи студент отримує стипендію
    def has_scholarship(self):
        return self.__average_grade is not None and self.__average_grade >= 4.5

    # 🔹 Новий метод 2: Перевіряє, чи студент випускається
    def is_graduating(self):
        return self.get_course() == 4  # Випуск на 4 курсі

    # 🔹 Гетер для приватного атрибута
    def get_average_grade(self):
        return self.__average_grade


# 🔹 Введення даних з консолі
name = input("Введіть ім'я: ")
surname = input("Введіть прізвище: ")

while True:
    try:
        birth_year = int(input("Введіть рік народження: "))
        break
    except ValueError:
        print("Будь ласка, введіть коректний рік народження (число).")

university = input("Введіть університет: ")
faculty = input("Введіть факультет: ")

while True:
    try:
        average_grade = float(input("Введіть середній бал (0-5): "))
        if 0 <= average_grade <= 5:
            break
        else:
            print("Будь ласка, введіть число від 0 до 5.")
    except ValueError:
        print("Будь ласка, введіть коректне число.")

# 🔹 Створення об'єкта
student = AdvancedStudent(name, surname, birth_year, university, faculty, average_grade)

# 🔹 Вивід інформації
print(f"Ім'я: {student.name}")
print(f"Прізвище: {student.surname}")
print(f"Рік народження: {student.birth_year}")
print(f"Курс: {student.get_course()}")
print(f"Університет: {student._university}")  # Захищений атрибут
print(f"Факультет: {student.faculty}")
print(f"Середній бал: {student.get_average_grade()}")

print(f"Отримує стипендію: {'Так' if student.has_scholarship() else 'Ні'}")
print(f"Чи випускається: {'Так' if student.is_graduating() else 'Ні'}")
