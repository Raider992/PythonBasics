'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''

'''
Создаём бесконечный цикл, начинаем ввод чисел, выход из цикла ставим на q(от англ. выход)
Предполагаем, что польхователь умеет читать, так что не вводим проверку на ошибки. 
Сначала находим количество уже присутствующих в списке введённых пользователем элементов
Если их нет, вставляем элемент, предварительно определив место, если есть, находим индекс последнего одинакового элемента
и вставляем после него
'''

rating = [15,10,6,5]

while True:
    user_input = input('Введите число рейтинга или q для конца ввода:\n')
    if user_input.lower() == 'q':
        print('ввод окончен')
        break
    element = int(user_input)

    element_count = rating.count(element)

    if not element_count:
        if element > rating[0]:
            rating.insert(0, element)
        elif element < rating[-1]:
            rating.append(element)
        else:
            for i, el in enumerate(rating):
                if el < element:
                    rating.insert(i, element)
                    break
    else:
        end_index = rating.index(element) + element_count
        rating.insert(end_index, element)

    print(rating)