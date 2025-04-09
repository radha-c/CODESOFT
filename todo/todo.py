from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

tasks = []  # In-memory storage (No database)

@app.route('/')
def home():
    return render_template('todo.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "id": str(len(tasks) + 1),
        "task": data['task'],
        "completed": False,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    return '', 201

@app.route('/delete/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return '', 204

@app.route('/toggle/<task_id>', methods=['PUT'])
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    return '', 200

if __name__ == '__main__':
    app.run(debug=True,port=5002)