""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper


@app.route("/delete/<int:task_id>", methods=['DELETE'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)


@app.route("/edit-status/<int:task_id>", methods=['PATCH'])
def update_status(task_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)






@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json() 
    db_helper.insert_new_task(data['description'],data['id'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/fetch-max-id",methods=['GET'])
def fetch_max_id():
    data = request.get_json()
    result= db_helper.fetch_max_id()
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)


