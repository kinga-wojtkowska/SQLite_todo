from flask import Flask, jsonify, abort, make_response, request
from todo_app.models import todos
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'to_do.db')


# wyświetla wszystkie rekordy w bazie
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
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)  # noqa: E501
