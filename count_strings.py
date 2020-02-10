#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

words = 0
lines = 0

with open('task_2.txt', 'r') as file:
    for line in file:               #проходим по строкам в файле, увеличиваем счётчик
        lines += 1
        position = 'out'
        for symbol in line:         #в строке проходим по символам, каждый раз, доходя до пробела, увеличиваем счётчик слов
            if symbol != ' ' and position == "out":
                words += 1
                position = 'in'
            elif symbol == ' ':
                position = 'out'

print(f"Строк: {lines}")
print(f"Слов: {words}")