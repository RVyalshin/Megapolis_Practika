from csv import *

array = []

with open('astronaut_time.txt', encoding='utf8') as file:
    reader = reader(file, delimiter=">")
    for el in reader:
        array.append(el)

dictionary = dict()

for el in array[1:]:
    dictionary[el[2]] = hash(el[2][3:])     #ключ - номер каюты, значение - хэш инфы о каюте

for el in range(1, 11):
    print(dictionary[array[el][2]])
