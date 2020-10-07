from todo_app.views import app
import sqlite3

app.config["SECRET_KEY"] = "nininini"


def create_connection(db_file):
    con = sqlite3.connect(db_file)
    return con


if __name__ == "__main__":

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
    cur.execute('INSERT INTO todo VALUES(NULL, ?, ?, ?);', ('cyk', 'biegi', 0))  # noqa: E501
    cur.execute('INSERT INTO todo VALUES(NULL, ?, ?, ?);', ('myk', 'rowerek', 0))  # noqa: E501
    cur.execute('INSERT INTO todo VALUES(NULL, ?, ?, ?);', ('fik', 'odpoczynek tez musi byc', 0))  # noqa: E501
    con.commit()

    exit()
