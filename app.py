from flask import Flask, jsonify, request 
app = Flask(__name__)
tasks = [   
    {
        'id': 1,  
        'title': 'Task 1',
        'description': 'This is task 1', 
        'done': False
    },
    {
        'id': 2,   
        'title': 'Task 2',
        'description': 'This is task 2',
        'done': False
    }
@app.route('/get-all-tasks', methods=['GET'])  
def get_tasks():
    return jsonify({'tasks': tasks})
@app.route('/get-task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({'task': task})
    else:
        return jsonify({'message': 'Task not found'}), 404
@app.route('/create-task', methods=['POST'])
def create_task():
    data = request.json  
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description'],
        'done': False
    }
    tasks.append(new_task)  
    return jsonify({'message': 'Task created successfully', 'task': new_task}), 201  
@app.route('/update-task/<int:task_id>', methods=['PUT']) 
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.json
        task.update(data)  
        return jsonify({'message': 'Task updated successfully', 'task': task})
    else:
        return jsonify({'message': 'Task not found'}), 404
@app.route('/delete-task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run()
