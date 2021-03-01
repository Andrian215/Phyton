tax_directory = []

def func(choose, standard):
    if choose == 1:
        for i in range(len(tax_directory)):
            if tax_directory[i]["Назва підприємства"] == standard:
                print(tax_directory[i])
    if choose == 2:
        for i in range(len(tax_directory)):
            if tax_directory[i]["Рівень оподаткування"] == standard:
                print(tax_directory[i])
    if choose == 3:
        for i in range(len(tax_directory)):
            if tax_directory[i]["Рік заснування"] == standard:
                print(tax_directory[i])
    if choose == 4:
        for i in range(len(tax_directory)):
            if tax_directory[i]["Власник"] == standard:
                print(tax_directory[i])

while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести дані про підприємство\n"
          "3. Знайти підприємство\n"
          "4. Вийти\n")
    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print(tax_directory)
    elif choose == 2:
        nameofcompany = input("Назва підприємства:")
        leveloftaxation = input("Рівень оподаткування:")
        leveloffoundation = int(input("Рік заснування:"))
        owner = input("Власник:")
        taxDict = {}
        "Заповнення словника"
        taxDict["Назва підприємства"] = nameofcompany
        taxDict["Рівень оподаткування"] = leveloftaxation
        taxDict["Рік заснування"] = leveloffoundation
        taxDict["Власник"] = owner
        tax_directory.append(taxDict)
        if leveloffoundation>2020 or leveloffoundation<=0:
            taxDict.clear()
            tax_directory.pop()
            print('Введіть реальну дату!')
            continue
    elif choose == 3:
        print("Знайти за:\n"
              "1.Назва підприємства\n"
              "2.Рівень оподаткування\n"
              "3.Рік заснування\n"
              "4.Власник\n")
        choose2 = int(input("Виберіть номер: "))
        if choose2 == 1:
            searchstandard = input("Введіть назву підприємства:")
            func(1, searchstandard)
        if choose2 == 2:
            searchstandard = input("Введіть рівень оподаткування:")
            func(2, searchstandard)
        if choose2 == 3:
            searchstandard = int(input("Введіть рік заснування:"))
            func(3, searchstandard)
        if choose2 == 4:
            searchstandard = input("Введіть власника:")
            func(4, searchstandard)
        if choose2 > 4 or choose2 <1:
            print('Введіть коректне значення!')
        print("\n")
    elif choose == 4:
        break
    else:
        print("Введіть коректне число\n")
