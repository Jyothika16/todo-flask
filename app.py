import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({"content": task, "status": "Pending"})
    return redirect(url_for('index'))

@app.route('/done/<int:task_id>')
def done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['status'] = "Done"
    return redirect(url_for('index'))

@app.route('/view')
def view():
    return render_template('view.html', tasks=tasks)

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    if request.method == 'POST':
        new_task = request.form['task']
        tasks[task_id]['content'] = new_task  # update task content
        return redirect(url_for('index'))
    return render_template('update.html', task=tasks[task_id], task_id=task_id)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
