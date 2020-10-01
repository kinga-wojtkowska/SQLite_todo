from todo_app.views import app
import sqlite3
import os

app.config["SECRET_KEY"] = "nininini"

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'to_do.db')


def create_connection(db_file):
    con = sqlite3.connect(db_file)
    return con


if __name__ == "__main__":

    app.run(debug=True)
    db_file = "todo_app/to_do.db"

    con = create_connection(db_file)
    cur = con.cursor()
    cur.executescript("""
        DROP TABLE IF EXISTS todo;
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY ASC,
            title varchar(250) NOT NULL,
            description varchar(250) NOT NULL,
            done_0_1 INTEGER NOT NULL
        )""")

    cur.execute('INSERT INTO todo VALUES(NULL, ?, ?, ?);', ('Sport', '30-minutowy spacer', 0))  # noqa: E501
    cur.execute('INSERT INTO todo VALUES(NULL, ?, ?, ?);', ('cyk', '30-minutowy spacer', 0))  # noqa: E501
    cur.execute('INSERT INTO todo VALUES(NULL, ?, ?, ?);', ('myk', '30-minutowy spacer', 0))  # noqa: E501
    cur.execute('INSERT INTO todo VALUES(NULL, ?, ?, ?);', ('fik', '30-minutowy spacer', 0))  # noqa: E501
    con.commit()
