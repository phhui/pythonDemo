from flask import Flask,request,Response
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_weorld():
    image = file("img/a.jpg") 
    resp = Response(image, mimetype="image/jpeg") 
    return resp

@app.route('/data',methods=['POST'])
def get_data():
    resp=Response('hello world',mimetype="text/html")
    return resp

@app.route('/getcookie',methods=['GET','POST'])
def set_cookie():
    resp=Response('hi xj',mimetype="text/html")
    resp.set_cookie('name','xj')
    return resp

@app.route('/readcookie',methods=['GET','POST'])
def read_cookie():
    name=request.cookies.get('name')
    print name
    return 'ok'

@app.after_request
def after_request(response):
#    response.headers.add('Access-Control-Allow-Origin','http://localhost:5329')
    response.headers.add('Access-Control-Allow-Origin','http://127.0.0.1:5329')
#    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Credentials','true')
    response.headers.add('Access-Control-Allow-Headers','Content-TYpe,Authorization,X-Requested-With')
    response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE')
    return response


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=80)
