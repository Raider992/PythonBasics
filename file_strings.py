#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def write_strings(*args):
    res = ''
    terminate = False
    for i in args:
        try:
            with open('task_1.txt', 'w') as file:
                file.write()
        except ValueError as e:
            if i == '\n':
                terminate = not terminate
    return res, terminate

while True:
    user_input = input("Введите строки, для выхода нажмите Enter повторно\n").split('\n')
    res_sum, terminate = write_strings(*user_input)
    sum +=res_sum
    print(f"сумма: {sum}")

    if terminate:
        print('Ввод окончен')
        break