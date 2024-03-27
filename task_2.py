from csv import *


def bubble_sort(array, len_array):
    """
    Сортировка пузырьком

    Ключевые значения:
    array - подаваемый список
    len_array - длина подаваемого списка
    """
    flag = True

    while flag:
        flag = False

        for el in range(len_array - 1):
            if int(array[el][1][:-4]) > int(array[el + 1][1][:-4]):
                array[el], array[el + 1] = array[el + 1], array[el]
                flag = True

    return array

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

array = array[1:]
array = bubble_sort(array, len(array))


for i in array[:3]:
    print(f'На станции {i[1]} в каюте {i[2]} восстановлено время. Актуальное время: {i[-1]}')