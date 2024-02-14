import csv


#Открываем файл и читаем его в список со словарями
with open(r'D:\мегаполис\practice\students.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',', quotechar='"')
    data = sorted(reader, key=lambda x: x['titleProject_id'])
    
id_pr = input()
    
while id_pr != 'СТОП':
    for row in data:
        if row['titleProject_id'] == id_pr:
            surname, name, patronymic = row['Name'].split()
            print(f'Проект № {id_pr} делал: {name[0]}. {surname} он(а) получил(а) оценку - {row["score"]}.')
            break
    else:
        print("Ничего не найдено")
    id_pr = input()
