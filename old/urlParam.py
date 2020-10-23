from flask import Flask
app=Flask(__name__)
@app.route('/login/<username>')
def login(username):
    return username

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=80)
