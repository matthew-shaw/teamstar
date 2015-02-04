from flask import Flask, render_template, request, redirect
from bson import json_util
import json
import pymongo

app = Flask(__name__)

# connecting to the database
conn = pymongo.Connection()
db = conn['mydb']
coll = db['teams']

@app.route('/add', methods=['POST'])
def add_team():
    name = request.form.get("name")
    coll.insert({"name": name})
    return redirect("/")

@app.route("/deleteall", methods=['GET'])
def deleteall():
    coll.remove()
    return redirect ("/")

@app.route('/find/<name>')
def find_team(name):
    result = [doc for doc in coll.find({"name": name})]
    return render_template('index.html', data=result)

@app.route('/')
def index():
    result = [doc for doc in coll.find()]
    return render_template('index.html', data=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
