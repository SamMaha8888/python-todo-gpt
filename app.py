from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection (change URI as per your setup)
client = MongoClient("mongodb://172.16.16.200:27017/")
db = client["todo_db"]
todos = db["tasks"]

@app.route("/")
def index():
    tasks = todos.find()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        todos.insert_one({"task": task})
    return redirect("/")

@app.route("/delete/<task>")
def delete_task(task):
    todos.delete_one({"task": task})
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
