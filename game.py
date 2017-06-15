from flask import MySQLdb,time,hashlib,Flask,request
app=Flask(__name__)
conn=MySQLdb.connect(host='localhost',user='phhui',passwd='phhuicom',db='ldsg',port=3306)
m=hashlib.md5()
keyStr='www.56lea.com'

def register(uid,key):
    res=execSql(uid,key)

@app.route('/login/',methods=['POST'])
def login():
    if request.methods=='POST':
	uid=request.form['openid']
	key=request.form['openkey']
	if validUser(uid):
	    if valid_login(uid,key):
	        key=keyStr+id+time.time()
                m.update(key)
  	        return m.hexdigest()
	else :
	    register(
    else :
	return 'err02'

def validUser(uid):
    res=execSql('select id from l_user where uid='+uid)
    if res!=False:
	return True
    else:
	return False

def valid_login(uid,key):
    res=execSql('select time from l_login where openid='+uid);
    if res!=False&time.time()-res<7200*1000:
	return True
    else:
	return False
	    

def execSql(sql):
    try:
	cur=conn.cursor()
        res=cur.execute(sql)
	info=cur.fetchmany(res)
        cur.close()
        conn.close
	return info
    except MySQLdb.Error,e:
        print 'Mysql Error %d: %s' % (e.args[0],e.args[1])
	return False

if __name=='__main__':
    app.debut=True
    app.run(host='0.0.0.0',port=80)
