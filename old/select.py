import MySQLdb

conn=MySQLdb.connect(host='localhost',user='phhui',passwd='phhuicom',db='ldsg',port=3306)


def sel(sql):
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
if __name__=='__main__':
    info=sel('select * from l_user')
    if info:
	for i in info:
	    print i
