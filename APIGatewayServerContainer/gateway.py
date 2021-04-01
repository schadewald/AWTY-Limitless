from flask import Flask,request,redirect,Response
import requests

app = Flask(__name__)
DB_RETRIEVE = 'http://nbadb:4321/db/'

@app.route('/')
def index():
    return "API Gateway is active"

@app.route('/retrieve',methods=['GET','POST',"DELETE"])
def proxy():
    global DB_RETRIEVE
    if request.method=='GET':
        resp = requests.get(f'{DB_RETRIEVE}retrieve')
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    #this currently does not need a POST methods, but going to leave here for future reference
    elif request.method=='POST':
        resp = requests.post(f'{DB_RETRIEVE}retrieve',json=request.get_json())
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    # this currently does not need a DELETE methods, but going to leave here for future reference
    elif request.method=='DELETE':
        resp = requests.delete(f'{DB_RETRIEVE}retrieve').content
        response = Response(resp.content, resp.status_code, headers)
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9999)