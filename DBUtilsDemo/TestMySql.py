#-*- coding: UTF-8 -*-  
'''
@描述：
@作者：CYH
@版本：V1.0
@创建时间：2016-11-24 上午9:34:54
'''
from DB_connetion_pool import getPTConnection, PTConnectionPool;

def TestMySQL():  
    #申请资源  
    with getPTConnection() as db:
        # SQL 查询语句;
        sql = "SELECT * FROM l_userinfo"
        try:
        # 获取所有记录列表
            db.cursor.execute(sql)
            results = db.cursor.fetchall();
            for row in results:
                userId = row[0]
                name= row[1]     
                sex= row[2]
                createTime = row[3]
                # 打印结果
                print ("userId=%d,name=%s,sex=%s,createTime=%s" %\(userId, name, sex, createTime ))
         except:
             print ("Error: unable to fecth data")
TestMySQL()
