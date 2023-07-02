import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(database="mydb", user='postgres', password='3326', host='localhost', port='5432')
# Создание курсора
cur = conn.cursor()

# Создание таблицы телефонов
cur.execute('''CREATE TABLE IF NOT EXISTS phones
    (id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    memory TEXT NOT NULL,
    ram TEXT NOT NULL,
    processor TEXT NOT NULL);''')
conn.commit()

# Получение списка всех телефоновw
def get_phones():
    cur.execute("SELECT * FROM phones")
    phones = cur.fetchall()
    return phones

# Добавление нового телефона
def create_phone(title, memory, ram, processor):
    cur.execute("INSERT INTO phones (title, memory, ram, processor) VALUES (%s, %s, %s, %s)",
                (title, memory, ram, processor))
    conn.commit()


# Удаление телефона из таблицы пользователей по названию
def delete_phone_by_title(title):
    cur.execute("DELETE FROM phones WHERE title = %s", (title,))
    conn.commit()


# Закрытие соединения с базой данных
# cur.close()
# conn.close()
