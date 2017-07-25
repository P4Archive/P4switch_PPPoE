#!flask/bin/python

from flask import Flask, jsonify, request, abort
import json

#clear function
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

#initialize session table in HWA 
session_table=[]
with open(r'/home/user/session_table.json', 'w') as outfile:  
         json.dump(session_table,outfile)

app = Flask(__name__)



@app.route('/hwa/delete_session/<int:session_id>', methods=['GET'])
def get_task(session_id):
    global session_table
    session = [session for session in session_table if session['session_id'] == session_id]
    if len(session) == 0:
        abort(404)
    session_table.remove(session[0])
    print "session table updated: {}".format(session_table)
    return json.dumps(session[0]), 201


@app.route('/hwa/session_table', methods=['POST'])
def update_session_table():
    if not request.json:
        abort(400)
    print request.json
    global session_table
    session_table=request.json
    jsonFile = open(r'/home/user/session_table.json', 'r+')
    deleteContent(jsonFile)
    jsonFile.write(json.dumps(session_table))
    print "session table updated: {}".format(session_table)
    return jsonify({'session_table': session_table}), 201

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000,debug=True)

