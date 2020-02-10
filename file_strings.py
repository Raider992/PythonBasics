# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_strings = []

while True:
    user_input = input('Введите строки, конец ввода - пустая строка\n')
    if user_input == '':
        break
    file_strings.append(user_input)

for i in file_strings:
    with open('task_1.txt', 'a') as file:
        file.write(f"{i}\n")