#-*- coding: UTF-8 -*-  
from DB_connetion_pool import *;
import json

def testMySQL():  
    #申请资源  
    with getPTConnection() as db:
        # SQL 查询语句;
        sql = "SELECT * FROM l_userinfo"
            # 获取所有记录列表
        db.cursor.execute(sql)
        results = db.cursor.fetchall()
        print json.dumps(results)
#        for row in results:
#            userId = row[0]
#            name= row[1]     
#            sex= row[2]
#            createTime = row[3]
            # 打印结果
#            print "userId="+str(userId)+",name="+str(name)+",sex="+str(sex)+"time="+str(createTime)
testMySQL()
