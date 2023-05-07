import sqlite3

# при запуске с маин надо полный путь
connection = sqlite3.connect('Database/db_bot.db')

# connection = sqlite3.connect('db_bot.db')
cursor = connection.cursor()


# sql - просто переменная (имя любое)
# далее заглавные это команды SQL (служебные слова) маленькие наши переменные

def create_users_table():
    sql = '''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR, tg_id INTEGER, login VARCHAR,password VARCHAR)'''
    cursor.execute(sql)
    connection.commit()


# def new_user(params: tuple[str, int, str, str]):
#     sql = '''INSERT INTO users (name, tg_id, login, password) VALUES (?, ?, ?, ?)'''
#     cursor.execute(sql, params)
#     print('добавлена запись -> ', params)
#     connection.commit()


def get_login_password(tg_id: int) -> tuple[str, str]:
    sql = '''SELECT login, password FROM users WHERE tg_id=?'''
    # передавать ТОЛЬКО кортеж (есди один элемент, то (елем,) элемент и запятая!!! в круглых скобках
    # когда что-то получаем из базы данных , то используем .fetch one(точно один)-all(все)-many(например, первые 5)

    # если fetchone то взвращает ОДИН кортеж
    # return cursor.execute(sql, (tg_id,)).fetchone()

    # если fetchall то взвращает СПИСОК кортежей
    return cursor.execute(sql, (tg_id,)).fetchall()

