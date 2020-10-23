from flask import Flask,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_weorld():
    return 'hello phhui'

@app.after_request
def after_request(response):
    response.headers.add('Access-COntrol-Allow-Origin','*')
    response.headers.add('Access-COntrol-Allow-Headers','Content-TYpe,Authorization')
    response.headers.add('Access-COntrol-Allow-Methods','GET,PUT,POST,DELETE')
    return response


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=80)
