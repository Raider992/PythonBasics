'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

seasons_d = {'Зима':(12,1,2),
             'Весна':(3,4,5),
             'Лето':(6,7,8),
             'Осень':(9,10,11)
            }

seasons_l = ['Зима','Весна','Лето','Осень']


month_input = int(input('Введите номер месяца'))

#Для словаря:

for key, value in seasons_d.items():
    if month_input in value:
        print(key)
        break
    break

#Для списка:

if month_input == 12 or month_input == 1 or month_input == 2:
    print(seasons_l[0])
elif month_input == 3 or month_input == 4 or month_input == 5:
    print(seasons_l[1])
elif month_input == 6 or month_input == 7 or month_input == 8:
    print(seasons_l[2])
elif month_input == 9 or month_input == 10 or month_input == 11:
    print(seasons_l[3])