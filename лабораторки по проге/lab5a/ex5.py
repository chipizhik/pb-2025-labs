messages = [
    {"user": "Исследователь А", "message": "Отчёт готов. Ссылка: http://foundation.org"},
    {"user": "Доктор Б", "message": "Документы можно найти здесь: https://classified.com"},
    {"user": "Охранник В", "message": "Нет аномальной активности за смену."},
    {"user": "Агент Г", "message": "Срочно изучите материалы по объекту 173 на http://statue-database.net"},
    {"user": "Д-р Кляйн", "message": "Обновлённый протокол эксперимента доступен: https://safezone.scp"},
    {"user": "Сотрудник Д", "message": "Просьба ознакомиться с https://docs.anomalies-secure.com перед сменой."},
    {"user": "Старший учёный Л", "message": "Все записи переданы. Никаких аномалий на объекте 096."},
    {"user": "Техник З", "message": "Проблема с сервером устранена. Подробнее: http://fix-report.internal"}
]
anomalies = list(filter(lambda meseage: 'http' in meseage["message"], messages))
remAnomalies = list(map(lambda meseage: {'user': meseage['user'],
                                         'message': meseage['message'].split('http')[0]+'[ДАННЫЕ УДАЛЕНЫ]'},messages))
for i in remAnomalies:
    print(i)