#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from statistics import mean

salaries = []

with open('task_3.txt', 'r', encoding="utf-8") as file:
    for employee in file:
        last_name, salary = employee.split(' ')
        salary = int(salary)
        if salary < 20000:
            print(last_name)
        salaries.append(salary)
    print(f"Средний оклад: {mean(salaries)}")