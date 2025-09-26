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
        tasks.append(task)
    return redirect(url_for('index'))
@app.route('/view')
def view():
    return render_template('view.html', tasks=tasks)
# Route to update a task
@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    if request.method == 'POST':
        new_task = request.form['task']
        tasks[task_id] = new_task  # replace old task with new one
        return redirect(url_for('index'))
    return render_template('update.html', task=tasks[task_id], task_id=task_id)



@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

