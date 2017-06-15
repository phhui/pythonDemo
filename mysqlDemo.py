import MySQLdb
try:
    conn=MySQLdb.connect(host='localhost',user='phhui',passwd='phhuicom',db='ldsg',port=3306)
    cur=conn.cursor()
    res=cur.execute('select * from l_user')
    info=cur.fetchmany(res)
    for i in info:
        print i
    cur.close()
    conn.close
except MySQLdb.Error,e:
    print 'Mysql Error %d: %s' % (e.args[0],e.args[1])
