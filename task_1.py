from csv import *


array = []

with open('astronaut_time.txt', encoding='utf8') as file:
    reader = reader(file, delimiter='>')
    for row in reader:
        array.append(row)

array_new = [["WatchNumber", 'numberStation', 'cabinNumber', 'timeStop', 'timeNow']]

for el in array[1:]:
    update_array = el
    update_array[-1] = str(int(el[-2][:2]) + int(el[-1]))
    if (int(update_array[-1]) >= 24) and ((int(update_array[-1]) - 24) < 10):
        update_array[-1] = f'0{str(int(update_array[-1]) - 24)}{update_array[-2][2:]}'
    elif (int(update_array[-1]) >= 24) and ((int(update_array[-1]) - 24) > 10):
        update_array[-1] = f'{str(int(update_array[-1]) - 24)}{update_array[-2][2:]}'
    elif int(update_array[-1]) < 10:
        update_array[-1] = f'0{update_array[-1]}{update_array[-2][2:]}'
    else:
        update_array[-1] = f'{update_array[-1]}{update_array[-2][2:]}'
    array_new.append(update_array)

with open("new_time.csv", "w", encoding='utf8', newline="") as file_csv:
    writer = writer(file_csv, delimiter=",")
    for el in array_new:
        writer.writerow(el)

for el in array_new:
    if el[2] == "98-OYE":
        print(f"{el[-1]} - действительное время для каюты: {el[2]}")
