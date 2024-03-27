from csv import *


array = []

with open('astronaut_time.txt', encoding='utf8') as file:
    reader = reader(file, delimiter='>')
    for row in reader:
        array.append(row)


chapter_1, chapter_2 = [], []


for el in array[1:]:
    sum_seconds = int(el[-2].split(":")[0]) * 60 * 60 + int(el[-2].split(":")[1]) * 60 + int(el[-2].split(":")[2])
    if 0 <= sum_seconds <= 43200:
        chapter_1.append(el[1])
    if 43201 <= sum_seconds <= 86399:
        chapter_2.append(el[1])

print(f'{len(chapter_1)} станций остановилось с период с 00.00 до 12.00.')
print(f'{len(chapter_2)} станций остановилось с период с 12.01 до 23.59.')