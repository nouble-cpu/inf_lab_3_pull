# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, rasd=','):
    '''
    входные группы

    и разделяем при помощи функции split по rasd

    дальше функция for проходит по фргументам в 2 группе и находи тсовпадение с другой

    возвращаем функцию сортируя его
    '''
    participants_first_group_spl = participants_first_group.split(rasd)         #созадние разделенного
    participants_second_group_spl = participants_second_group.split(rasd)       #оже самое
    reslult = []                                                                #Создаем список всех кто и там, и там
    for i in participants_second_group_spl:                                     #обьяснение так то же было свепху
        if i in participants_first_group_spl:
            reslult.append(i)                                                   #вооот забыл про него, функция append для присоединения к списку
    return sorted(reslult)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))