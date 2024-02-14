import csv


def generate_hash(s):
    alphabet = [chr(x) for x in range(1040,1104)]+[' ']+['ё'] + ['Ё']
    p = 67
    m = 10**9+9
    hash_value = sum([(alphabet.index((s[i]))*p**i) for i in range(len(s))])%m
    return hash_value

student_with_hash = []


with open(r'students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file,delimiter=',', quotechar='"'))
    for row in reader:
        row['id'] = generate_hash(row['Name'])
        student_with_hash.append(row)


with open(r'D:\мегаполис\practice\students_with_hash.csv', 'w', encoding='utf-8', newline='') as file:
    reader = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    reader.writeheader()
    reader.writerows(student_with_hash)
