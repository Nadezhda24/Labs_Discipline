class Disciplin:

    def __init__(self, id, name, first_name,
                 second_name, exam, coursework,
                 count_lec, count_pr,count_lab = 0):
        self.id = id  #код
        self.name = name #название
        self.first_name = first_name #имя  преподователя
        self.second_name = second_name #фамиля преподователя
        self.exam = exam #форма контроля
        self.coursework = coursework #наличие курсовой 1-есть, 0-нет
        self.count_lec = count_lec #кол-во лек
        self.count_pr = count_pr #кол-во пр
        self.count_lab = count_lab #кол-во лаб


    def showInfo(self):
        print("|%-7s|%-15s|%-15s|%-15s|%-6s|%-10s|%-11s|%-15s|%-10s|" % (str(self.id), self.name, self.first_name , self.second_name ,  self.exam, str(self.coursework), str(self.count_lec), self.count_pr , str(self.count_lab)))


person = [Disciplin(1, "math" , "Person1", "Person1", "exam", 1, 12, 2, 8),
Disciplin(2,"Python", "Person2", "Person2", "test", 0, 12, 2, 8)]

while True:
    try:
        k = int(input("==========================\n"
                      "1. Добавление информации.\n"
                      "2. Удаление информации.\n"
                      "3. Отображение информации.\n"
                      "4. Поиск по форме контроля.\n"
                      "Для выхода введите 0.\n"
                      "Введите номер задания: "))
    except:
        print("Ошибка, введен не верный номер задания. Попробуйте снова.")
        continue
    break

while k != 0:
    if k == 1:
        while True:
            try:
                id = int(input("Код: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        name = (input("Название дисциплины: "))
        first_name = (input("Имя: "))
        second_name = (input("Фамилия: "))
        exam = (input("Форма контроля: "))
        while True:
            try:
                coursework = (input("Наличие курсовой: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        while True:
            try:
                count_lec = int(input("Количество лекций: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break

        while True:
            try:
                count_pr = (input("Количество практик: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        while True:
            try:
                count_lab = int(input("Количество лабораторных: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        if (count_lab < 0):
         person.append(Disciplin(id, name, first_name,
                 second_name, exam, coursework,
                 count_lec, count_pr))
        else:
            person.append(Disciplin(id, name, first_name,
                                  second_name, exam, coursework,
                                  count_lec, count_pr, count_lab ))
    elif k == 2:
        # удаление по номеру элемента в списке начиная с 0
        while True:
            try:
                x = int(input("Номер для удаления: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        for i in range(len(person)):
            if(i == x):
                person.pop(i)
    elif k == 3:
        print("|%-7s|%-15s|%-15s|%-15s|%-6s|%-10s|%-11s|%-15s|%-10s|" % ("id", "name", "first_name", "second_name", "exam", "coursework","count_lec","count_pr","count_lab"))
        for i in range(len(person)):
            person[i].showInfo()
    elif k == 4:
        while True:
            try:
                x = (input("Форма контроля: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        f = False
        for i in range(len(person)):
            if (person[i].exam == x):
                f = True
                person[i].showInfo()
        if not(f):
            print("Дисциплин с этой формой контроля нет.")
    else: print("Ошибка, введен не верный номер задания. Попробуйте снова.")

    while True:
        try:
            k = int(input("==========================\n"
                      "1. Добавление информации.\n"
                      "2. Удаление информации.\n"
                      "3. Отображение информации.\n"
                      "4. Поиск по форме контроля.\n"
                      "Для выхода введите 0.\n"
                      "Введите номер задания: "))
        except:
            print("Ошибка, введен не верный номер задания. Попробуйте снова.")
            continue
        break