import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS countries
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)''')


countries = ['Испания', 'США', 'Россия']
cursor.executemany('INSERT INTO countries (title) VALUES (?)', [(country,) for country in countries])


cursor.execute('''CREATE TABLE IF NOT EXISTS cities
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL,
                  area REAL DEFAULT 0, country_id INTEGER,
                  FOREIGN KEY(country_id) REFERENCES countries(id))''')


cities = [('Москва', 2561.5, 1), ('Нью-Йорк', 789.4, 2), ('Париж', 105.4, 3),
          ('Лондон', 1572.0, 3), ('Токио', 2188.0, 5), ('Сидней', 2058.0, 6),
          ('Каир', 3085.0, 7)]
cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)


cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL, city_id INTEGER,
                  FOREIGN KEY(city_id) REFERENCES cities(id))''')


employees = [('Иван', 'Иванов', 1), ('Петр', 'Петров', 1), ('Алексей', 'Сидоров', 2),
             ('Елена', 'Петрова', 2), ('Анна', 'Козлова', 3), ('Дмитрий', 'Смирнов', 3),
             ('Наталья', 'Васильева', 4), ('Мария', 'Попова', 4), ('Денис', 'Ильин', 5),
             ('Сергей', 'Кузнецов', 5), ('Екатерина', 'Морозова', 6), ('Ольга', 'Николаева', 6),
             ('Артем', 'Ковалев', 7), ('Максим', 'Зайцев', 7), ('Юлия', 'Соловьева', 7)]
cursor.executemany('INSERT INTO employees (first_name, last_name, city_id) VALUES (?, ?, ?)', employees)


while True:
    print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(city[0], city[1])
    city_id = int(input("Введите id города: "))
    if city_id == 0:
        break
    else:

        cursor.execute('''SELECT e.first_name, e.last_name, c.title, ct.title
                          FROM employees e
                          INNER JOIN cities c ON e.city_id = c.id
                          INNER JOIN countries ct ON c.country_id = ct.id
                          WHERE c.id = ?''', (city_id,))
        employees = cursor.fetchall()
        if employees:
            for employee in employees:
                print("Имя:", employee[0])
                print("Фамилия:", employee[1])
                print("Страна:", employee[2])
                print("Город проживания:", employee[3])
                print()
        else:
            print("Нет сотрудников, проживающих в выбранном городе.")
        print()


conn.close()
