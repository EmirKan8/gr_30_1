import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL
                )''')


countries = [('Испания',), ('Финляндия',), ('Швейцария',)]
cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries)
conn.commit()


cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    area REAL DEFAULT 0,
                    country_id INTEGER,
                    FOREIGN KEY (country_id) REFERENCES countries(id)
                )''')


cities = [('Москва', 2561.4, 1),
          ('Нью-Йорк', 789.4, 2),
          ('Париж', 105.4, 3),
          ('Лондон', 1572.0, 3),
          ('Токио', 2190.93, 4),
          ('Рим', 1285.3, 3),
          ('Сидней', 2058.0, 5)]
cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)
conn.commit()


cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    city_id INTEGER,
                    FOREIGN KEY (city_id) REFERENCES cities(id)
                )''')


employees = [('Иван', 'Петров', 1),
             ('John', 'Doe', 2),
             ('Jean', 'Dupont', 3),
             ('Алексей', 'Иванов', 1),
             ('Jane', 'Smith', 4),
             ('Пьер', 'Мартин', 3),
             ('Emily', 'Johnson', 5),
             ('Мария', 'Сидорова', 6),
             ('Michael', 'Brown', 2),
             ('Анна', 'Ковалева', 1),
             ('William', 'Taylor', 2),
             ('София', 'Лебедева', 3),
             ('David', 'Wilson', 4),
             ('Александра', 'Попова', 6),
             ('Andrew', 'Jones', 5)]
cursor.executemany('INSERT INTO employees (first_name, last_name, city_id) VALUES (?, ?, ?)', employees)
conn.commit()


print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")


cursor.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()
for city in cities:
    print(city[0], city[1])


while True:
    city_id = input("Введите id города: ")
    if city_id == '0':
        break
    cursor.execute('''SELECT e.first_name, e.last_name, ct.title AS country, c.title AS city
                      FROM employees e
                      JOIN cities c ON e.city_id = c.id
                      JOIN countries ct ON c.country_id = ct.id
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
        print("Таких сотрудников нет")

conn.close()