print("имя и количество золотых монет")

import sqlite3


class DataBase:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('score')

    def create_table(self, table_name):
        que = f"""CREATE TABLE IF NOT EXISTS {table_name} (
            id INGER PRIMARY KEY,
            name TEXT,
            score_point INTEGER
        ) 
        """
        self.cur.execute(que)
        self.con.commit()

    def get(self, que='SELECT * FROM score'):
        return self.cur.execute(que).fetchall()

    def insert(self, name, score):
        que = f"""INSERT INTO score (name, score_point) VALUES ('{name}', {score})"""
        self.cur.execute(que)
        self.con.commit()

    def __del__(self):
        self.con.close()


db = DataBase('score.sqlite3')
db.insert('кот милорд', 300)
db.insert('мистер скрудж', 1000)
db.insert('злотой кот-лем', 100000000)
list = db.get()
list = sorted(list, key=lambda x: -x[2])
for i in list:
    print(i)
