# Tkinter_homework

Это самостоятельная работа - учебный проект создания десктопного приложения на Python + PostgreSQL с применением библиотеки tkinter + psycopg2

--- При старте приложения выводится меню с возможностью выбора действий: 1 – авторизироваться, 2 – зарегистрироваться

<img width="824" alt="image_2023-03-07_02-38-27" src="https://github.com/RntNur/Tkinter_homework/assets/115574135/2ed6cfbf-5098-4113-bb83-21a22912b995">
<img width="822" alt="image_2023-03-07_02-38-27 (3)" src="https://github.com/RntNur/Tkinter_homework/assets/115574135/87a5f5c7-f033-41ab-b29e-58b2ac1b0e1e">

--- Пользователь может войти с помощью логина и пароля. Введенные данные проверяются с таблицы Пользователей в БД. Если пользователь логически не существует (exist == false), то пользователь не может войти в систему.
--- Если пользователь авторизовался как посетитель ему доступен функционал просмотра доступных телефонов для "покупки".
<img width="833" alt="image_2023-03-07_02-38-27 (2)" src="https://github.com/RntNur/Tkinter_homework/assets/115574135/59488555-cff0-41c5-9d15-88fa2a3a3b64">

--- Если пользователь авторизовался как администратор ему доступен функционал добавления товаров, удаления товаров, просмотр информации о пользователях, смена роли пользователю.
--- По умолчанию все пользователи регистрируются как посетители. Роль посетителю можно сменить только администратор.
<img width="835" alt="image_2023-03-07_02-37-19" src="https://github.com/RntNur/Tkinter_homework/assets/115574135/83c46263-5bcb-4278-a0fe-27dc3e020121">

# Запуск программы:

1) Создать базу данных + Настроить модули 'users.py' и 'phones.py':
  # Установить пакет psycopg2:
    pip install psycopg2
  # Подключение к базе данных:
    conn = psycopg2.connect(database="mydb", user='postgres', password='3326', host='localhost', port='5432')
    
2) Запустить исполняемый файл 'tk.py'
   
