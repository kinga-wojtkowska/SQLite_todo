from flask import Flask, request
import sqlite3
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'to_do.db')

class Todos:
    def __init__(self, con, cur):
        self.con = con
        self.cur = cur


    def all(self):
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        tasks = cur.execute('SELECT * FROM todo').fetchall()
        return tasks


    def get(self, todo_id):
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        todo = cur.execute('SELECT * FROM todo WHERE id=?', (todo_id,)).fetchone()
        if todo:
            return todo
        return []


    def create(self):
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        datareq = request.json
        todo = (datareq['title'], datareq.get('description', ""), datareq['done_0_1'])
        cur.execute('INSERT INTO todo VALUES(NULL, ?, ?, ?);', todo)
        con.commit()
        return todo


    def save_all(self):
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        con.commit()


    def update(self, todo_id):
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        todo = cur.execute("SELECT * FROM todo WHERE id=?", (todo_id,)).fetchone()
        datareq = request.json
        title = datareq.get('title', todo[1])
        description = datareq.get('description', todo[2])
        done_0_1 = datareq.get('done_0_1', todo[3])
        cur.execute("""UPDATE todo
                    SET title = ?,
                    description = ?,
                    done_0_1 = ?
                    WHERE id = ?""", (title, description, done_0_1, todo_id,))
        con.commit()
        updated = cur.execute("SELECT * FROM todo WHERE id=?", (todo_id,)).fetchone()  # noqa: E501
        return updated


    def delete(self, todo_id):
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        to_delete = cur.execute("SELECT * FROM todo WHERE id=?", (todo_id,)).fetchone()  # noqa: E501
        cur.execute("DELETE FROM todo WHERE id=?", (todo_id,))
        con.commit()
        return to_delete
      

con = sqlite3.connect(db_file)
cur = con.cursor()
todos = Todos(con, cur)