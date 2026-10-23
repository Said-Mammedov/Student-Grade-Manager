name = ""
surname = ""
age = 0
grades = []

while True:
    print("\n------Калькурятор для оценивания студента------")
    print("\t1. Ввести данные студента")
    print("\t2. Добавить оценку")
    print("\t3. Показать все оценки")
    print("\t4. Рассчитать итоговый результат")
    print("\t5. Выход")


    choise = input("\t\tВыберите действие от 1-го до 5-ти: ").strip()


    if choise == "1":
        name = input("Введите имя: ").strip()

        while name == "":
            print("Имя не может быть пустым!")
            name = input("Введите имя: ").strip()

        surname = input("Введите фамилию: ").strip()

        while surname == "":
            print("Фамилия не может быть пустой!")
            surname = input("Введите фамилию: ").strip()

        age = int(input("Введите возраст: "))

        while age < 5 or age > 100:
            print("Возраст должен быть от 5 до 100!")
            age = int(input("Введите возраст: "))

        grades = []

        print("Профиль студента успешно создан!")


    elif choise == "2":
        if name == "" or surname == "":
            print("Сначала создайте профиль студента!")
        else:
            grade = int(input("Введите оценку от 0 до 100: "))

            while grade < 0 or grade > 100:
                print("Ошибка! Оценка должна быть от 0 до 100!")
                grade = int(input("Введите оценку от 0 до 100: "))

            grades.append(grade)
            print("Оценка успешно добавлена!")



    elif choise == "3":

        if name == "" or surname == "":

            print("Сначала создайте профиль студента!")

        elif len(grades) == 0:

            print("Оценок пока нет!")

        else:

            print("\n------ Все оценки ------")

            for i in range(len(grades)):
                print(i + 1, "-", grades[i])





    elif choise == "4":

        if name == "" or surname == "":

            print("Сначала создайте профиль студента!")

        elif len(grades) == 0:

            print("Сначала добавьте хотя бы одну оценку!")

        else:

            total = 0

            maximum = grades[0]

            minimum = grades[0]

            for grade in grades:

                total = total + grade

                if grade > maximum:
                    maximum = grade

                if grade < minimum:
                    minimum = grade

            average = total / len(grades)

            if average >= 90:

                category = "A"

                description = "Отлично"

            elif average >= 80:

                category = "B"

                description = "Хорошо"

            elif average >= 70:

                category = "C"

                description = "Удовлетворительно"

            elif average >= 60:

                category = "D"

                description = "Слабо"

            else:

                category = "F"

                description = "Неудовлетворительно"

            if average >= 60:

                status = "Сдал"

            else:

                status = "Не сдал"

            print("\n------ Итоговый отчёт ------")

            print("ФИО:", name, surname)

            print("Возраст:", age)

            print("Все оценки:", grades)

            print("Количество оценок:", len(grades))

            print("Средний балл:", round(average, 2))

            print("Максимальная оценка:", maximum)

            print("Минимальная оценка:", minimum)

            print("Категория:", category)

            print("Описание:", description)

            print("Статус:", status)


    elif choise == "5":
        print("\t\tВыход из программы!")
        break
    else:
        print("\t\tНадо ввести число от 1-го до 5-ти!!!")

    print("Hello")








