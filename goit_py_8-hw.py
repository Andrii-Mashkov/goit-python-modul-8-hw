'''
Функция get_birthdays_per_week предназначена для вывода списка коллег, 
которых надо поздравить с днём рождения на неделе (в рабочие дни).
Пользователей, у которых день рождения был на выходных (суббота и воскресенье), надо поздравить в понедельник.
Функция выводит пользователей с днями рождения на неделю вперед от текущего дня.
Неделя начинается с понедельника.

Функция получает на вход список users.
Функция выводит в консоль (при помощи print) список пользователей, 
которых надо поздравить по дням недели (наименования на английском языке).
Функция ничего не возвращает (возвращает None).

Список словарей users: каждый словарь обязательно имеет ключи name и birthday: 
    name — это строка с именем пользователя,
    birthday — это datetime объект, в котором записан день рождения.
Такая структура представляет модель списка пользователей с их именами и днями рождения. 

Функция выводит именинников в формате:
Monday: Bill, Jill
Friday: Kim, Jan

Для отладки создан тестовый:
- список users, который заполнен самостоятельно (строки 123-...),
- спсикок "текущих дат" (строки 40-50).
'''
# Импортируем функционал для работы с датами и временем
from datetime import datetime, timedelta

def get_birthdays_per_week(users: list) -> None:
    
    # Список списков именниников по дням недели
    result = [[],[],[],[],[]]

    # Наименование жней недели
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Определяем текущую дату
    today_date = datetime.today().date()
    
    # Для отладки
    # today_string = '29-07-2023' # Суббота
    # today_string = '30-07-2023' # Воскресенье
    # today_string = '31-07-2023' # Понедельник
    # today_string = '01-08-2023' # Вторник
    # today_string = '28-12-2022' # Среда
    # today_string = '31-12-2022' # Суббота
    # today_string = '01-01-2023' # Воскресенье
    # today_string = '02-01-2023' # Понедельник
    # today_string = '03-01-2023' # Вторник
    # today_date = datetime.strptime(today_string, '%d-%m-%Y')
    
    # Определяем день недели текущей даты
    today_weekday = today_date.weekday()

    # Если текущий день это суббота или воскресенье, то поздравлять будем в понедельник
    # и переносим текущую дату на понедельник
    if today_weekday > 4:
        today_date = today_date + timedelta(days = 7-today_weekday)
        today_weekday = 0
   
    # Определяем период дней рождения именинников
    if today_weekday == 0:
        date_begin = today_date - timedelta(days=2)
        date_end   = today_date + timedelta(days=4)
    else:
        date_begin = today_date 
        date_end   = today_date + timedelta(days=6)
    
    # Определяем год, к которому будем вприводить все даты дней рождения
    date_year  = date_begin.year

    # Формируем списки именников в периоде
    for item in users:
        
        # Приводим дату дня рождения именинника к установленному ранее году
        # причем, если еть переход года, то для дат января принимаем следующий год
        birthday = item["birthday"]
        d, m = birthday.day, birthday.month
        if date_begin.year != date_end.year and  m == 1:
                date_item = datetime(year=date_year+1, day=d, month=m).date()
        else:
            date_item = datetime(year=date_year, day=d, month=m).date()

        # Берем именниников в нужном интервале
        if date_begin <= date_item <= date_end:
            
            #  Определяем день недели иименинника
            item_weekday = date_item.weekday()
            
            # Если день рождения в субботу или воскресенье, то поздравлять будем в понедельник
            if item_weekday > 4:
               item_weekday = 0
            
            # Добавляем имя именниника в соответствующий день недели
            result[item_weekday].append(item["name"])

    # Определяем день недели с которого надо начинать вывод.
    # если текущий день недели суббота или воскресенье, то выводим с понедельника, иначе с текущего дня недели
    current_weekday = today_weekday
    if current_weekday > 4:
        current_weekday = 0

    # Вывод результата (пять списков)  
    for item in range(5):
        
        # Выбираем из соответствующего списка наименование дня недели
        day_name = day_names[current_weekday]

        # Переводим список имен в строку
        srt_names = ', '.join(result[current_weekday])
        
        # Выводим наименование дня недели и строку (список имен именинников) 
        print(f'{day_name}: {srt_names}')
        
        # Вычисляем следующий день недели
        current_weekday += 1

        # Если номер дня недели больше пятницы (4), то переходим на понедельник (0)
        if current_weekday > 4:
            current_weekday = 0
# конец функции

# для отладки
users = [
    {"name": "Anna",   "birthday": datetime.strptime("27-07-2000", "%d-%m-%Y")}, # weekday = 3
    {"name": "Boris",  "birthday": datetime.strptime("28-07-2000", "%d-%m-%Y")}, # weekday = 4
    {"name": "Celena", "birthday": datetime.strptime("29-07-2000", "%d-%m-%Y")}, # weekday = 5
    {"name": "Danilo", "birthday": datetime.strptime("30-07-2000", "%d-%m-%Y")}, # weekday = 6
    {"name": "Eva",    "birthday": datetime.strptime("31-07-2000", "%d-%m-%Y")}, # weekday = 0
    {"name": "Fedor",  "birthday": datetime.strptime("01-08-2000", "%d-%m-%Y")}, # weekday = 1
    {"name": "Grigor", "birthday": datetime.strptime("02-08-2000", "%d-%m-%Y")}, # weekday = 2
    {"name": "Helena", "birthday": datetime.strptime("03-08-2000", "%d-%m-%Y")}, # weekday = 3
    {"name": "Ivan",   "birthday": datetime.strptime("04-08-2000", "%d-%m-%Y")}, # weekday = 4
    {"name": "Jeck",   "birthday": datetime.strptime("05-08-2000", "%d-%m-%Y")}, # weekday = 5
    {"name": "Kell",   "birthday": datetime.strptime("06-08-2000", "%d-%m-%Y")}, # weekday = 6
    {"name": "Maks",   "birthday": datetime.strptime("07-08-2000", "%d-%m-%Y")}, # weekday = 0
    {"name": "Nidl",   "birthday": datetime.strptime("08-08-2000", "%d-%m-%Y")}, # weekday = 1
    {"name": "Olga",   "birthday": datetime.strptime("09-08-2000", "%d-%m-%Y")}, # weekday = 2
    {"name": "Petro",  "birthday": datetime.strptime("10-08-2000", "%d-%m-%Y")}, # weekday = 3
    {"name": "Red",    "birthday": datetime.strptime("11-08-2000", "%d-%m-%Y")}, # weekday = 4
    {"name": "Sem",    "birthday": datetime.strptime("12-08-2000", "%d-%m-%Y")}, # weekday = 5
    {"name": "Tim",    "birthday": datetime.strptime("13-08-2000", "%d-%m-%Y")}, # weekday = 6
    {"name": "N-28",   "birthday": datetime.strptime("28-12-2000", "%d-%m-%Y")}, # weekday = 3
    {"name": "N-29",   "birthday": datetime.strptime("29-12-2000", "%d-%m-%Y")}, # weekday = 4
    {"name": "N-30",   "birthday": datetime.strptime("30-12-2000", "%d-%m-%Y")}, # weekday = 5
    {"name": "N-31",   "birthday": datetime.strptime("31-12-2000", "%d-%m-%Y")}, # weekday = 6
    {"name": "N-01",   "birthday": datetime.strptime("01-01-2001", "%d-%m-%Y")}, # weekday = 0
    {"name": "N-02",   "birthday": datetime.strptime("02-01-2001", "%d-%m-%Y")}, # weekday = 1
    {"name": "N-03",   "birthday": datetime.strptime("03-01-2001", "%d-%m-%Y")}, # weekday = 2
    {"name": "N-04",   "birthday": datetime.strptime("04-01-2001", "%d-%m-%Y")}, # weekday = 3
    {"name": "N-05",   "birthday": datetime.strptime("05-01-2001", "%d-%m-%Y")}, # weekday = 4
    {"name": "N-06",   "birthday": datetime.strptime("06-01-2001", "%d-%m-%Y")}, # weekday = 5
    {"name": "N-07",   "birthday": datetime.strptime("07-01-2001", "%d-%m-%Y")}, # weekday = 6
]

if __name__ == "__main__":
    get_birthdays_per_week(users)
