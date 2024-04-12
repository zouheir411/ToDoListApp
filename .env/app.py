from flask import Flask,render_template,request,redirect,url_for
app= Flask(__name__,template_folder='templates')

todos = [{"todo":"Sample","done":False}]
@app.route("/")
def index():
    return render_template("index.html",todos=todos)

@app.route("/add",methods=["POST"])
def add() :
    todo=request.form['todo']
    todos.append({"todo":todo,"done":False})
    return redirect(url_for("index"))
@app.route("/edit/<int:index>",methods=['POST','GET'])
def edit (index):
    todo = todos[index]
    if request.method=='POST':
        todo['todo']=request.form['todo']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html",todo=todo,index=index)

@app.route('/check/<int:index>')
def check(index):
    todos[index]['done']= not todos[index]['done']
    return redirect(url_for("index")) 

@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for("index"))
if __name__=='__main__':
    app.run('127.0.0.1',debug=True,port=5500)


