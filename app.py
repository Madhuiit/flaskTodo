from flask import Flask,render_template,request,jsonify,flash,abort
app = Flask(__name__)
app.secret_key = '123' #requerd for falsk message
#in memeory storage for task (use a database in production)
tasks = []

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if not task:
            flash('task can not be empty')
        else:
            tasks.append({'id':len(tasks)+1,'task':task})
        return render_template('index.html',tasks=tasks)
    return render_template('index.html',tasks=tasks)

@app.route('/delete/<int:task_id>',methods=['GET','POST'])
def delete_task(task_id):
    #find and remove tasks
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'success':True})
    abort(400,description='Task not found')
@app.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify(tasks)
if __name__=='__main__':
    app.run(debug = True)

    

