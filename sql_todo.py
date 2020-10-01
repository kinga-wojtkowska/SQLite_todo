from flask import Flask, jsonify, abort, make_response, request
from .todo_app import views
from .todo_app.models import todos
import sqlite3
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'to_do.db')


def create_connection(db_file):
    con = sqlite3.connect(db_file)
    return con


'''# wyświetla wszystkie rekordy w bazie
@app.route("/api/sql/todos/", methods=["GET"])
def todos_list_sql():
    return jsonify(todos.all())


# tworzy nowy rekord w bazie
@app.route("/api/sql/todos/", methods=["POST"])
def create_todo():
    if not request.json or 'title' not in request.json:
        abort(400)
    todo = todos.create()
    return jsonify({'todo': todo}), 201


# pokazuje konkretny rekord z bazy danych
@app.route("/api/sql/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        abort(404)
    return str(todo)


# usuwa rekord o konkretnym id z bazy danych
@app.route("/api/sql/todos/<int:todo_id>", methods=['DELETE'])
def delete_todo(todo_id):
    to_delete = todos.delete(todo_id)
    if not to_delete:
        abort(404)
    return f'the record below has been deleted: {to_delete}'


# aktualizacja rekordu w bazie danych
@app.route("/api/sql/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = todos.get(todo_id)
    if not request.json or not todo:
        abort(400)
    updated = todos.update(todo_id)
    return f'the record below has been updated: {updated}'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)  # noqa: E501


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)  # noqa: E501'''


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
