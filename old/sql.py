import MySQLdb
class sqlHelper:
    conn=MySQLdb.connect(host='localhost',user='phhui',passwd='phhuicom',db='ldsg',port=3306)

    def __init__(self):
	print 'init'


    @classmethod
    def select(self,sql,params=None):
	try:
            cur=self.conn.cursor()
            res=cur.execute(sql,params)
            cur.close()
            self.conn.close
	    return True
	except MySQLdb.Error,e:
	    print 'Mysql Error %d: %s' % (e.args[0],e.args[1])
	    return 'error'

    def selectVal(self,sql,params=None):
	try:
            cur=self.conn.cursor()
            res=cur.execute(sql,params)
            info=cur.fetchmany(res)
            cur.close()
            self.conn.close
	    return info
	except MySQLdb.Error,e:
	    print 'Mysql Error %d: %s' % (e.args[0],e.args[1])
	    return 'error'

    @classmethod
    def update(self,sql,params=None):
	try:
            cur=self.conn.cursor()
            res=cur.execute(sql,params)
	    self.conn.commit()
            cur.close()
            self.conn.close
	    return True
	except MySQLdb.Error,e:
	    print 'Mysql Error %d: %s' % (e.args[0],e.args[1])
	    return 'error'
