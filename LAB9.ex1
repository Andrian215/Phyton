student_directory = []

def func(choose, standard):
    if choose == 1:
        for i in range(len(student_directory)):
            if student_directory[i]["Номер маршруту"] == standard:
                print(student_directory[i])
    if choose == 2:
        for i in range(len(student_directory)):
            if student_directory[i]["Кінцева зупинка"] == standard:
                print(student_directory[i])
    if choose == 3:
        for i in range(len(student_directory)):
            if student_directory[i]["Номер автобуса"] == standard:
                print(student_directory[i])
    if choose == 4:
        for i in range(len(student_directory)):
            if student_directory[i]["Час поїздки"] == standard:
                print(student_directory[i])

while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні про маршрут\n"
          "3. Знайти маршрут\n"
          "4. Вийти\n")
    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print(student_directory)
    elif choose == 2:
        routenumber = int(input("Введіть номер маршруту: "))
        laststop = input("Введіть кінцеву зупинку: ")
        busbrand = input("Введіть марку автобуса: ")
        traveltime = int(input("Час поїздки(в хвилинах): "))
        studentDict = {}
        "Заповнення словника"
        studentDict["Номер маршруту"] = routenumber
        studentDict["Кінцева зупинка"] = laststop
        studentDict["Марка автобуса"] = busbrand
        studentDict["Час поїздки"] = traveltime
        student_directory.append(studentDict)
    elif choose == 3:
        print("Знайти за:\n"
              "1.Номер маршруту\n"
              "2.Кінцева зупинка\n"
              "3.Марка автобуса\n"
              "4.Час поїздки\n")
        choose2 = int(input("Виберіть номер: "))
        if choose2 == 1:
            searchstandard = int(input("Введіть номер маршруту: "))
            func(1, searchstandard)
        if choose2 == 2:
            searchstandard = input("Введіть кінцеву зупинку: ")
            func(2, searchstandard)
        if choose2 == 3:
            searchstandard = input("Введіть марку автобуса: ")
            func(3, searchstandard)
        if choose2 == 4:
            searchstandard = int(input("Введіть час поїздки(в хвилинах): "))
            func(4, searchstandard)
        print("\n")
    elif choose == 4:
        break
    else:
        print("Введіть коректне число\n")
