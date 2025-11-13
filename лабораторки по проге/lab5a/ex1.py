tasks = [("Проверить почту", 31), ("Написать отчёт", 111), ("Позвонить клиенту", 2), ("позвонить клиенту", 4)]
sorted_tasks = sorted(tasks, key=lambda task: task[1])
print(sorted_tasks)