from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with (open('./root.json', 'r') as file):
    root=json.load(file.read())

@app.route('/v1/getscriptlistbyfirstletter')
def getscriptlistbyfirstletter():
    firstletter = request.args.get('')
    scriptsnum = int(root['scriptsnumber'])
    for i in range(scriptsnum - 1):
        if root['scripts']['script{}'.format(i)]['name'][0] == firstletter:
            return jsonify(root['scripts']['script{}'.format(i)])


@app.route('/v1/getinfobyname')
def getinfobyname():
    scriptname = request.args.get('scrnme')
    scriptsnum = int(root['scriptsnumber'])
    for i in range(scriptsnum-1):
        if root['scripts']['script{}'.format(i)]['name'] == scriptname:
            return jsonify(root['scripts']['script{}'.format(i)])
    return jsonify({"status": "error", "message": "The script with name {} doesn't exist".format(scriptname)})
@app.route('/v1/getinfobyid')
def getinfobyid():
    scriptid = request.args.get('scrid')
    try:
        return jsonify(root['scripts']['script{}'.format(scriptid)])
    except KeyError:
        return jsonify({"status" : "error", "message" : "The script with ID {} doesn't exist".format(scriptid)})