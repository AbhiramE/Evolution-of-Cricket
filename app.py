from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGO_USERNAME = 'admin'
MONGO_PASSWORD = 'admin123'
DBS_NAME = 'match_details'
COLLECTION_NAME = 'dv'
FIELDS = {
    "_id": False,
    "": True,
    "Team": True,
    "ScoreDescending": True,
    "Overs": True,
    "RPO": True,
    "Inns": True,
    "Result": True,
    "Opposition": True,
    "Ground": True,
    "Start_Date": True,
    "Year": True,
    "Runs": True,
    "Range": True
}

BATSMEN_DB = 'batsmen_records_years_wise'
FIELDS_BATSMEN = {
    "_id": False,
    "": True,
    "Player": True,
    "Team": True,
    "Mat": True,
    "Inns": True,
    "NO": True,
    "RunsDescending": True,
    "HS": True,
    "Ave": True,
    "BF": True,
    "SR": True,
    "100": True,
    "50": True,
    "0": True,
    "4s": True,
    "6s": True,
    "Season": True,
    "SR_Range": True
}

BOWLERS_DB = 'bowlers_records_years_wise'
FIELDS_BOWLERS = {
    "_id": False,
    "": True,
    "Player": True,
    "Team": True,
    "Mat": True,
    "Inns": True,
    "Overs": True,
    "Mdns": True,
    "Runs": True,
    "WktsDescending": True,
    "BBI": True,
    "Ave": True,
    "Econ": True,
    "SR": True,
    "4": True,
    "5": True,
    "Season": True
}


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/indexBatsmen.html")
def index_batsmen():
    return render_template("indexBatsmen.html")


@app.route("/indexBowlers.html")
def index_bowlers():
    return render_template("indexBowlers.html")


@app.route("/match_details/projects")
def match_details_projects():
    connection = MongoClient('mongodb://admin:admin123@localhost:27017/')
    print connection
    collection = connection[DBS_NAME][COLLECTION_NAME]
    print collection
    projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


@app.route("/batsmen/projects")
def batsmen_projects():
    connection = MongoClient('mongodb://admin:admin123@localhost:27017/')
    print connection
    collection = connection[BATSMEN_DB][COLLECTION_NAME]
    print collection
    projects = collection.find(projection=FIELDS_BATSMEN)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


@app.route("/bowlers/projects")
def bowlers_projects():
    connection = MongoClient('mongodb://admin:admin123@localhost:27017/')
    print connection
    collection = connection[BOWLERS_DB][COLLECTION_NAME]
    print collection
    projects = collection.find(projection=FIELDS_BOWLERS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
