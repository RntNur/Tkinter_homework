import tkinter as tk
from tkinter import ttk
from phones import create_phone, delete_phone_by_title, get_phones
from users import authenticate_user, get_users, update_role, register_user, delete_user_by_id


# Создание главного окна
root = tk.Tk()
root.title("Магазин телефонов")
root.state('zoomed')

# Создание объектов вкладок
tab_control = ttk.Notebook(root)
user_tab = ttk.Frame(tab_control)
admin_tab = ttk.Frame(tab_control)
enter_tab = ttk.Frame(tab_control)
reg_tab = ttk.Frame(tab_control)
tab_control.add(enter_tab, text="Вход")  # Вкладка входа и кнопка регистрация
tab_control.add(reg_tab, text="Регистрация")
tab_control.hide(reg_tab) # Скрыть вкладку "Регистрация"
tab_control.add(user_tab, text="Пользователь")
tab_control.hide(user_tab)  # Скрыть вкладку "Пользователь"
tab_control.add(admin_tab, text="Администратор")
tab_control.hide(admin_tab)  # Скрыть вкладку "Администратор"
tab_control.pack(fill="both")
# f_left = Frame(admin_tab)
# f_right = Frame(admin_tab)


# Функции для обработки & нажатий кнопок
def login():
    username = login_entry.get()
    password = password_entry.get()
    user_role = authenticate_user(username, password)  # обращение к модулю users.py с введенными данными в аргументах
    if user_role == "user":
        tab_control.select(user_tab)
        tab_control.show(user_tab)  # отобразить вкладку если роль admin
    elif user_role == "admin":
        tab_control.select(admin_tab)
        tab_control.show(admin_tab)  # отобразить вкладку если роль admin
    else:
        error_label.config(text="Неправильный логин или пароль")

def reg():
    tab_control.select(reg_tab)
    tab_control.show(reg_tab)  # Открыть вкладку регистрации пользователя


def register():
    fio = fio_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    register_user(fio, username, password)
    success_label.config(text="Регистрация прошла успешно")


def show_phones_admin():
    # Очистить список телефонов перед обновлением
    phone_listbox_admin.delete(*phone_listbox_admin.get_children())
    phones = get_phones()  # Взять данные из БД через модуль phones.py
    for phone in phones:
        phone_listbox_admin.insert("", "end", values=phone)


def show_phones_user():
    # Очистить список телефонов перед обновлением
    phone_listbox_user.delete(*phone_listbox_user.get_children())
    phones = get_phones()
    for phone in phones:
        phone_listbox_user.insert("", "end", values=phone)


def show_users_admin():
    user_listbox_admin.delete(*user_listbox_admin.get_children())
    users = get_users()
    for user in users:
        user_listbox_admin.insert("", "end", values=user)


def add_phone():
    name = name_entry.get()
    memory = memory_entry.get()
    ram = ram_entry.get()
    processor = processor_entry.get()
    create_phone(name, memory, ram, processor)
    success_label_1.config(text="Телефон успешно добавлен")
    show_phones_admin()


def delete_phone():
    selected_phone = phone_entry.get()
    delete_phone_by_title(selected_phone)
    success_label_1.config(text="Телефон успешно удален")
    show_phones_admin()


def delete_user():
    # selection = user_listbox_admin.selection()
    # item = user_listbox_admin.item(selection)
    # user_id = item["values"][1] --- способ выбора строки в таблице указателем
    user_id = user_id_entry.get()
    delete_user_by_id(user_id)
    show_users_admin()


def change_role():
    selection = user_listbox_admin.selection()
    item = user_listbox_admin.item(selection)
    selected_user = item["values"][4]
    username = item["values"][2]
    if selected_user == "user":
        new_role = "admin"
        update_role(username, new_role)
    else:
        new_role = "user"
        update_role(username, new_role)
    success_label_2.config(text="Роль пользователя успешно изменена")
    show_users_admin()


# Создание виджетов на вкладке "Вход"
login_label = tk.Label(enter_tab, text="Логин:")
login_label.pack()
login_entry = tk.Entry(enter_tab)
login_entry.pack()

password_label = tk.Label(enter_tab, text="Пароль:")
password_label.pack()
password_entry = tk.Entry(enter_tab, show="*")
password_entry.pack()

login_button = tk.Button(enter_tab, text="Войти", command=login)
login_button.pack()
error_label = tk.Label(enter_tab, fg="red")
error_label.pack()

register_button = tk.Button(enter_tab, text="Регистрация", command=reg)
register_button.pack()

instruction_label = tk.Label(enter_tab, text="Введите свой логин и пароль или зарегистрируйтесь")
instruction_label.pack()

# Открыть вкладку регистрации
fio_label = tk.Label(reg_tab, text="Введите Ф.И.О.: ")
fio_label.pack(padx=5)
fio_entry = tk.Entry(reg_tab)
fio_entry.pack()

username_label = tk.Label(reg_tab, text="Введите логин: ")
username_label.pack(padx=5)
username_entry = tk.Entry(reg_tab)
username_entry.pack()

pass_label = tk.Label(reg_tab, text="Введите пароль: ")
pass_label.pack(padx=5)
pass_entry = tk.Entry(reg_tab)
pass_entry.pack()

reg_button = tk.Button(reg_tab, text="Зарегистрироваться", command=register)
reg_button.pack(pady=20)
exit_button = tk.Button(reg_tab, text="Выход", command=reg_tab.destroy)
exit_button.pack(pady=20)

success_label = tk.Label(reg_tab, fg="green")
success_label.pack()


"""# Создание виджетов на вкладке "Пользователь"""

exit_button = tk.Button(user_tab, text="Выход", command=user_tab.destroy)
exit_button.pack(anchor="n")

phone_label = ttk.Label(user_tab, text="Телефоны")
phone_label.pack(pady=30)

phone_listbox_user = ttk.Treeview(user_tab, columns=("id", "title", "memory", "ram", "processor"))
# Установить текст посередине для всех столбцов
for col in phone_listbox_user['columns']:
    phone_listbox_user.column(col, anchor='center')
# Задать ширину столбцов
phone_listbox_user.column("#0", width=0)
phone_listbox_user.column("#1", width=30)
phone_listbox_user.column("#3", width=100)
phone_listbox_user.column("#4", width=40)
phone_listbox_user.column("#5", width=300)
# Задать столбцы таблицы телефонов
phone_listbox_user.heading("id", text="id")
phone_listbox_user.heading("title", text="Модель")
phone_listbox_user.heading("memory", text="Память")
phone_listbox_user.heading("ram", text="ОЗУ")
phone_listbox_user.heading("processor", text="Процессор")
phone_listbox_user.pack()
show_phones_user()


"""# Создание виджетов на вкладке "Администратор"""

admin_left_frame = ttk.Frame(admin_tab, width=290, height=400)  # Создание левого и правого фрейма-контейнера
admin_right_frame = ttk.Frame(admin_tab, width=290, height=400)
admin_left_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
admin_right_frame.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.BOTH, expand=True)


# Добавление виджетов в левую колонку вкладки "Администратор"
admin_left_label = ttk.Label(admin_left_frame)
admin_left_label.pack(pady=10)

phone_label = ttk.Label(admin_left_label, text="Телефоны")
phone_label.pack(pady=30)

phone_listbox_admin = ttk.Treeview(admin_left_label, columns=("id", "title", "memory", "ram", "processor"))
# Установить опцию anchor для всех столбцов
for col in phone_listbox_admin['columns']:
    phone_listbox_admin.column(col, anchor='center')
# Задать ширину столбцов
phone_listbox_admin.column("#0", width=0)
phone_listbox_admin.column("#1", width=30)
phone_listbox_admin.column("#3", width=100)
phone_listbox_admin.column("#4", width=40)
phone_listbox_admin.column("#5", width=300)
# Задать столбцы таблицы
phone_listbox_admin.heading("id", text="id")
phone_listbox_admin.heading("title", text="Модель")
phone_listbox_admin.heading("memory", text="Память")
phone_listbox_admin.heading("ram", text="ОЗУ")
phone_listbox_admin.heading("processor", text="Процессор")
phone_listbox_admin.pack()
show_phones_admin()

# Удаление телефона
phone_delete = ttk.Label(admin_left_label, text="Введите название телефона")
phone_delete.pack()
phone_entry = ttk.Entry(admin_left_label)
phone_entry.pack()

delete_phones_button = tk.Button(admin_left_label, text="Удалить телефон", command=delete_phone)
delete_phones_button.pack()

# Ввести данные телефона для добавления
add_phone_label = ttk.Label(admin_left_label, text="Добавить телефон")
add_phone_label.pack(pady=10)

name_label = ttk.Label(admin_left_label, text="Название")
name_label.pack()
name_entry = ttk.Entry(name_label)
name_entry.pack(padx=100)

memory_label = ttk.Label(admin_left_label, text="Память")
memory_label.pack()
memory_entry = ttk.Entry(memory_label)
memory_entry.pack(padx=100)

ram_label = ttk.Label(admin_left_label, text="ОЗУ")
ram_label.pack()
ram_entry = ttk.Entry(ram_label)
ram_entry.pack(padx=100)

processor_label = ttk.Label(admin_left_label, text="Процессор")
processor_label.pack()
processor_entry = ttk.Entry(processor_label)
processor_entry.pack(padx=100)

add_phone_button = ttk.Button(admin_left_label, text="Добавить", command=add_phone)
add_phone_button.pack()
success_label_1 = tk.Label(admin_left_label, fg="green")
success_label_1.pack()


# Добавление виджетов в правую колонку вкладки "Администратор"
admin_right_label = ttk.Label(admin_right_frame)
admin_right_label.pack(pady=10)

exit_button = tk.Button(admin_right_label, text="Выход", command=admin_tab.destroy)
exit_button.pack(anchor="ne")

users_label = ttk.Label(admin_right_label, text="Управление пользователями")
users_label.pack(pady=30)
# Отобразить список пользователей
user_listbox_admin = ttk.Treeview(admin_right_label, columns=("id", "fio", "username", "password", "role", "exists"))
for col in user_listbox_admin['columns']:
    user_listbox_admin.column(col, anchor='center')
# Задать ширину столбцов
user_listbox_admin.column("#0", width=0)
user_listbox_admin.column("#1", width=20)
user_listbox_admin.column("#2", width=200)
user_listbox_admin.column("#3", width=100)
user_listbox_admin.column("#4", width=50)
user_listbox_admin.column("#5", width=50)
user_listbox_admin.heading("id", text="id")
user_listbox_admin.heading("fio", text="fio")
user_listbox_admin.heading("username", text="username")
user_listbox_admin.heading("role", text="role")
user_listbox_admin.heading("password", text="password")
user_listbox_admin.heading("exists", text="exists")
user_listbox_admin.pack()
show_users_admin()

user_id_label = tk.Label(admin_right_label, text="Укажите id отключаемого пользователя")
user_id_label.pack(pady=5)
user_id_entry = ttk.Entry(admin_right_label)
user_id_entry.pack(pady=5)
delete_users_button = tk.Button(admin_right_label, text="Отключить пользователя", command=delete_user)
delete_users_button.pack(pady=5)

# Сменить роль юзера

change_role_button = tk.Button(admin_right_label, text="Изменить роль", command=change_role)
change_role_button.pack()
success_label_2 = tk.Label(admin_right_label, fg="green")
success_label_2.pack()
# Запуск программы
root.mainloop()
