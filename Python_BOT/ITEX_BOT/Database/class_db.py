import sqlite3


class DataBase:
    def __init__(self, db_path: str = 'Database/db_bot.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table(self, table_name: str):
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} (id PRIMARY KEY, name TEXT, age INT, comment TEXT)'
        self.execute(sql, commit=True)

    def new_user(self, params: tuple[str, int, str, str]):
        sql = '''INSERT INTO users (name, tg_id, login, password) VALUES (?, ?, ?, ?)'''
        self.execute(sql, params, commit=True)

    def find_user(self, table_name: str, **kwargs):
        sql = f'SELECT * FROM {table_name} WHERE '
        sql, params = self.extract_kwargs(sql, kwargs)
        print(sql)
        print(params)
        self.execute(sql, params, fetchall=True)


    @staticmethod
    def extract_kwargs(sql: str, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{key} = ?' for key in parameters])
        return sql, tuple(parameters.values())











    def disconnect(self):
        self.connection.close()








    # def new_user(params: tuple[str, int, str, str]):
    #     sql = '''INSERT INTO users (name, tg_id, login, password) VALUES (?, ?, ?, ?)'''
    #     cursor.execute(sql, params)
    #     print('добавлена запись -> ', params)
    #     connection.commit()
    # #     def __str__(self):
    #         return f'меня зовут {self.name} и мне {self.age} лет'
    #
    #
    #
    # obj1 = DBClass('STOME', 38)
    #
    # print(obj1)
