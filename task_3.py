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


while True:
    cab_number = input()
    if cab_number == "none":
        break
    flag_local = []
    for el in array_new[1:]:
        if cab_number == el[2]:
            flag_local.append(el[-2])
            flag_local.append(el[-1])
            break
    if len(flag_local) != 0:
        print(f'В каюте {cab_number} восстановлено время (время остановки: {flag_local[0]}). Актуальное время: {flag_local[-1]}')
    else:
        print('В этой каюте все хорошо')


