from flask import Flask
app = Flask(__name__)
from flask import request
import json

def override_workers(workers_):
    workers = dict()
    workers["workers"] = workers_
    with open("workers.json", "w") as fo:
        fo.write(json.dumps(workers))

def get_workers_json():
    workers = []
    with open('workers.json') as json_file:
        workers = json.load(json_file)
    return workers

@app.route('/addWorker')
def addWorker():
    if request.args.get('name') and request.args.get('id'):
        worker = create_worker(request.args.get('name'),request.args.get('id'),"FREE")
        workers = get_workers_json()
        workers["workers"].append(worker)
        override_workers(workers["workers"])
        return "granted"
    return "failed"

@app.route('/removeWorker')
def removeWorker():
    pass

def create_worker(name,id,status):
    worker = dict()
    worker["name"] = name
    worker["id"] = id
    worker["status"] = status
    return worker

@app.route('/init')
def initBabe():
    workers = []
    workers.append(create_worker("Mateusz","832","FREE"))
    workers.append(create_worker("Sofia","8332","FREE"))
    workers.append(create_worker("Alba","8132","FREE"))
    override_workers(workers)
    return "yees"

@app.route('/')
def index():
    return "yees"

@app.route('/workers', methods=['GET'])
def get_workers():
    return get_workers_json()

@app.route('/update_workers', methods=['POST'])
def update_workers():
    print(request.get_json())
    override_workers(request.get_json())
    return "updated"
app.run()