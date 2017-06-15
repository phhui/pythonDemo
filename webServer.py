from flask import abort,redirect,url_for

@app.route('/')
def index():
    return 'hello'

@app.route('/getKey')
def getKey():
    return "phhui.com"

@app.route('save/<key,data>',methods=['POST'])
def save(key,data):
    if request.method=='POST':
        return 'post'
     else:
        return 'nopost'


