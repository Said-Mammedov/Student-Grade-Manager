
students = []
grades = []


def add_student():
    name = input("Введите имя студента: ")

    if name in students:
        print("Ошибка! Такой студент уже существует.")
        return

    try:
        grade = int(input("Введите оценку (0-100): "))
    except ValueError:
        print("Ошибка! Нужно ввести число.")
        return

    if grade < 0 or grade > 100:
        print("Ошибка! Оценка должна быть от 0 до 100.")
        return

    students.append(name)
    grades.append(grade)

    print("Студент успешно добавлен!")


def show_students():
    print("\nСПИСОК СТУДЕНТОВ:")

    if len(students) == 0:
        print("Список пуст.")
        return

    for i in range(len(students)):
        print(students[i], "-", grades[i])


def find_student():
    name = input("Введите имя студента: ")

    if name in students:
        index = students.index(name)
        print("Студент:", students[index])
        print("Оценка:", grades[index])
    else:
        print("Студент не найден.")


def update_grade():
    name = input("Введите имя студента: ")

    if name in students:
        index = students.index(name)

        try:
            grade = int(input("Введите новую оценку (0-100): "))
        except ValueError:
            print("Ошибка! Нужно ввести число.")
            return

        if grade < 0 or grade > 100:
            print("Ошибка! Оценка должна быть от 0 до 100.")
            return

        grades[index] = grade

        print("Оценка успешно изменена!")
    else:
        print("Студент не найден.")


def delete_student():
    name = input("Введите имя студента: ")

    if name in students:
        index = students.index(name)

        students.pop(index)
        grades.pop(index)

        print("Студент успешно удалён!")
    else:
        print("Студент не найден.")


def average_grade():
    if len(grades) == 0:
        print("Нет оценок для вычисления среднего балла.")
        return

    average = sum(grades) / len(grades)

    print("Средний балл:", average)


def best_student():
    if len(grades) == 0:
        print("Список студентов пуст.")
        return

    index = grades.index(max(grades))

    print("Лучший студент:", students[index])
    print("Его оценка:", grades[index])


def passed_students():
    found = False

    print("\nСТУДЕНТЫ С ОЦЕНКОЙ 50 И ВЫШЕ:")

    for i in range(len(students)):
        if grades[i] >= 50:
            print(students[i], "-", grades[i])
            found = True

    if not found:
        print("Таких студентов нет.")


def menu():
    while True:
        print("""
************** МЕНЮ ПРОГРАММЫ **************

1. Добавить студента
2. Показать всех студентов
3. Найти студента
4. Изменить оценку
5. Удалить студента
6. Средний балл
7. Лучший студент
8. Сдавшие студенты
0. Выход

********************************************
""")

        try:
            choice = int(input("Введите номер команды (0-8): "))
        except ValueError:
            print("Ошибка! Введите число.")
            continue

        if choice == 1:
            add_student()

        elif choice == 2:
            show_students()

        elif choice == 3:
            find_student()

        elif choice == 4:
            update_grade()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            average_grade()

        elif choice == 7:
            best_student()

        elif choice == 8:
            passed_students()

        elif choice == 0:
            print("Программа завершена!")
            break

        else:
            print("Неверная команда! Попробуйте снова.")


menu()
