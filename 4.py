import csv
import string
import random

def create_initials(s:string):
    '''
    В функцию поступает строка(s) - ФИО, записанное через пробел
    Функция возвращает логин пользователя в формате <Фамилия_ИИ>
    '''
    names = s.split(' ')
    return f'{names[0]}_{names[1][0]}{names[2][0]}'



def create_password():
    '''
    В функцию ничего не поступает
    Возвращает функция пароль, длиной 8 символов, случайно сгенерированный из букв кодировки ascii и цифр
    '''
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


students_with_passwords = []
 

#Открываем файл, читаем построчно содержимое, и записываем в новый список, добавляя логи и пароль
with open(r'D:\мегаполис\practice\students.csv', encoding = 'utf-8') as file:
    reader = list(csv.DictReader(file,delimiter=',',quotechar='"'))
    for row in reader:
        row['login'] = create_initials(row['Name'])
        row['password'] = create_password()
        students_with_passwords.append(row)

#Записываем список в новый файл
with open(r'D:\мегаполис\practice\students_new.csv', 'w', newline='', encoding = 'utf-8') as file:
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    w.writeheader()
    w.writerows(students_with_passwords)
