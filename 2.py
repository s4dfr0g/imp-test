import csv


#открываем файл
with open(r'D:\мегаполис\practice\students.csv', encoding='utf-8') as file:
    #читаем файл в лист в формате [[row],[row],[row]]
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))

    #Далее сортировка вставками
    for i in range(1,len(reader)):
        key = i
        while (float(reader[key]['score']) if reader[key]['score'] != 'None' else 0) < (float(reader[key-1]['score']) if reader[key-1]['score'] != 'None' else 0) and key != 0:
            reader[key], reader[key-1] = reader[key-1], reader[key]
            key -= 1


print('10 класс')
#Счетчик места
count = 1

#Выводим людей, если класс равен 10, в нужном формате ("первая буква имени. фамилия")
for el in reversed(reader):
    if '10' in el['class']:
        surname, name, patronumic = el['Name'].split()
        print(f'{count} место: {name[0]}. {surname}')
        count += 1
    if count == 4:
        break
