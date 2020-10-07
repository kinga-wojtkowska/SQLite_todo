#ZADANIA To-Do
1. Run app.bat - it sets FLASK_ENV to development mode and run server
2. In another window call 'python sql_todo.py' - it creates db and table todo inside
3. After that you can start testing:
    a) GET http://localhost:5000/api/sql/todos/ - shows all records in the database
    b) POST http://localhost:5000/api/sql/todos/ - allows to add new record to the database
       parameters should be given: title, description and done_0_1
       param done_0_1 is integer value, 1 for True and 0 for False for readability
    c) GET http://localhost:5000/api/sql/todos/todo_id - where todo_id is the record number
       display a record with given id
    d) DELETE http://localhost:5000/api/sql/todos/todo_id - where todo_id is the record number
       delete a record with given id
    e) PUT http://localhost:5000/api/sql/todos/todo_id - where todo_id is the record number
       allows to change data in a record with given id,
       any of the parameters listed can be changed: title, description or done_0_1