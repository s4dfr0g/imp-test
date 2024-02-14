import csv


#открываем файл
with open(r'D:\мегаполис\practice\students.csv', encoding='utf-8') as file:
    #читаем файл в лист в формате [[row],[row],[row]]
    reader = csv.reader(file, delimiter=',')
    #Перебираем каждый лист и ищем тот, в котором имя и фамилия совпадают с искомым
    for row in reader:
        if 'Хадаров Владимир' in row[1]:
            print(f'Ты получил {row[4]}, за проект {row[2]}')
