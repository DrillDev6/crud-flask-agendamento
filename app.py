from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

#CRUD = CREATE, READ, UPDATE, DELETE

#Tabela = task
tasks = []
task_id_control = 1

@app.route ('/tasks', methods= ['POST'])
#CREATE
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], descriptions=data.get('descriptions'), completed=data.get('completed') )
    #eu poderia acessar o title com title=data.get['title']
    task_id_control += 1
    tasks.append(new_task)
    print (tasks)
    return jsonify({"message": 'Nova tarefa criada com sucesso', "id": new_task.id})

@app.route('/tasks', methods=['GET'])
#READ
def get_tasks():
    task_list = [task.to_dict() for task in tasks ]

    output= {
            "tasks": task_list,
            "descripitions": 'descriptions',
            "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
#Chamar tarefa especifica
def get_task(id):
    for t in tasks:
        if t.id == id:
            return (t.to_dict())

    return jsonify({"message": "Não foi possivel encontra a tarefa especificada"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
#UPDATE
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a tarefa!"}), 404
    print
    data = request.get_json()
    task.title = data['title']
    task.descriptions = data['descriptions']
    task.completed = data['completed']
    print(task)
    return jsonify ({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a tarefa"}), 404

    tasks.remove(task)
    return jsonify({"message": "A tarefa foi deleteda com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)

