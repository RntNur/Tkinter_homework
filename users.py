import psycopg2


# Подключение к базе данных
conn = psycopg2.connect(database="mydb", user='postgres', password='3326', host='localhost', port='5432')
# Создание курсора
cur = conn.cursor()

# Создание таблицы пользователей
cur.execute('''CREATE TABLE IF NOT EXISTS users
    (id SERIAL PRIMARY KEY,
    fio TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    exist BOOLEAN NOT NULL);''')
conn.commit()

# Добавление нового пользователя
def register_user(fio, username, password):
    try:
        cur.execute(
            "INSERT INTO users (fio, username, password, role, exist) VALUES (%s, %s, %s, %s, %s)",
            (fio, username, password, 'user', True))
        conn.commit()
        return True
    except psycopg2.Error:
        return False


    # Проверка аутентификации пользователя
def authenticate_user(username, password):
    global cur
    try:
        cur.execute("SELECT role,exist FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchall()  #получение списка с кортежем свойств выбранных атрибутов - role,exist FROM user
        # далее извлекаю и проверяю на соответствие значения из переменнной user
        if user[0][0] == 'user' and user[0][1]:  # условием user[0][1] проверяю наличие True по указанному индексу
            user_role = "user"
            return user_role
        elif user[0][0] == 'admin' and user[0][1]:
            user_role = "admin"
            return user_role
        else:
            return None
    except psycopg2.Error as error:
        print(error)


    # Получение списка всех пользователей
def get_users():
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users


    # Изменение роли пользователя
def update_role(username, role):
    cur.execute("UPDATE users SET role = %s WHERE username = %s", (role, username))
    conn.commit()

    # Удаление телефона из таблицы пользователей по названию
def delete_user_by_id(id):
    cur.execute("UPDATE users SET exist = NOT exist WHERE id = %s", (id,))
    conn.commit()


# Закрытие соединения с базой данных
# cur.close()
# conn.close()