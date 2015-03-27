from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)

# connecting to the database
conn = pymongo.Connection()
db = conn['mydb']
coll = db['people']

@app.route('/addmember', methods=['POST'])
def add_member():
    name = request.form.get("name")
    email = request.form.get("email")
    twitter = request.form.get("twitter")
    slack = request.form.get("slack")
    github = request.form.get("github")
    mobile = request.form.get("mobile")
    team = request.form.get("team")
    db['people'].insert({"name": name, "email": email, "mobile": mobile, "twitter": twitter, "slack": slack, "github": github, "team": team})
    return redirect("/")

@app.route('/addteam', methods=['POST'])
def add_team():
    name = request.form.get("name")
    db['teams'].insert({"name": name})
    return redirect("/")

@app.route("/deleteallmembers", methods=['GET'])
def deleteallmembers():
    db['people'].remove()
    return redirect ("/")

@app.route("/deleteallteams", methods=['GET'])
def deleteallteams():
    db['teams'].remove()
    return redirect ("/")

@app.route('/find/<name>', methods=["GET"])
def find_team(name):
    result = [doc for doc in coll.find({"name": name})]
    return render_template('index.html', data=result)

@app.route('/', methods=["GET"])
def index():
    teams = [doc for doc in db['teams'].find()]
    members = [doc for doc in db['people'].find()]
    return render_template('index.html', teams=teams, members=members)

@app.route('/update', methods=['POST'])
def update():
    coll.update()
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
