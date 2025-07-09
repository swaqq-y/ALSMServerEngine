from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with (open('./root.json', 'r') as file):
    root=json.load(file.read())
@app.route('/v1/getscriptpathbyid')
def getscriptpathbyid():
    scriptid = request.args.get('scrid')
    try:
        return "/{}".format(root["scripts"]["script{}".format(scriptid)])
    except KeyError:
        return jsonify({"status" : "error", "message" : "The script with ID {} doesn't exist".format(scriptid)})

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

"""@app.route('/api/startsession')
def startsession():
    global usrdb
    walsdid = request.args.get('walsdid')
    password = request.args.get('password')
    if walsdid not in usrdb:
        usrdb[walsdid] = {'download' : {}, 'password':'password'}
        usrdb[walsdid]['password'] = password
        return jsonify({'status' : 'done', 'message' : "APIRESULT_200"})
    else:
        return jsonify({'status': 'error', 'message': 'APIERROR_600'.format(walsdid)})

@app.route('/api/closesession')
def closesession():
    walsdid = request.args.get('walsdid')
    password = request.args.get('password')
    if not password:
        return jsonify({'status': 'error', 'message': 'APIERROR_501'})
    if not walsdid:
        return jsonify({'status' : 'error', 'message':'APIERROR_500'})
    if walsdid not in usrdb:
        return jsonify({"status": 'error', 'message': "APIERROR_300"})
    if password == usrdb[walsdid]['password']:
        del usrdb[walsdid]
        return jsonify({'status' : 'done', 'message' : 'APIRESULT_200'})
    else:
        return jsonify({'status' : 'error', 'message':'APIERROR_200'})
@app.route('/')
def mainpage():
    return render_template("index.html")
@app.route('/WALSTDocs')
def walstwiki():
    return render_template("WALSTWiki.html")
@app.route('/api/downloads')
def download():
    walsdid = request.args.get('walsdid')
    usrdbnum = request.args.get('usrdbn')
    password = request.args.get('password')
    if not usrdbnum:
        return jsonify({'status': 'error', 'message': 'APIERROR_501'})
    if not walsdid:
        return jsonify({'status' : 'error', 'message':'APIERROR_500'})
    if walsdid not in usrdb:
        return jsonify({"status": 'error', 'message': "APIERROR_300"})
    if password == usrdb[walsdid]['password']:
        return jsonify({'scriptname' : usrdb[walsdid]['download'][usrdbnum]})

@app.route('/api/getdownloads')
def getdownloads():
    walsdid = request.args.get('walsdid')
    password = request.args.get('password')
    if not walsdid:
        return jsonify({'status': 'error', 'message': 'APIERROR_500'})
    if walsdid not in usrdb:
        return jsonify({"status": 'error', 'message': "APIERROR_300"})
    if password == usrdb[walsdid]['password']:
        return jsonify({'status': 'done', 'content': usrdb[walsdid]['download']})
@app.route('/api/adddownload')
def adddownload():
    global usrdb
    walsdid = request.args.get('walsdid')
    password = request.args.get('password')
    scriptname = request.args.get('scrnme')
    scriptnumber = request.args.get('scrnmb')
    if not scriptnumber:
        return jsonify({'status': 'error', 'message': 'APIERROR_500'})
    if not walsdid:
        return jsonify({'status': 'error', 'message': 'APIERROR_500'})
    if not scriptname:
        return jsonify({'status': 'error', 'message': 'APIERROR_502'})
    if walsdid not in usrdb:
        return jsonify({"status": 'error', 'message': "APIERROR_300"})
    if not password:
        return jsonify({'status': 'error', 'message': 'APIERROR_500'})
    if password == usrdb[walsdid]['password']:
        usrdb[walsdid]['download'][scriptnumber] = scriptname
        return jsonify({'status': 'done', 'message': 'APIRESULT_200'})
    else:
        return jsonify({'status' : "error", 'message' : 'APIERROR_200'})

"""