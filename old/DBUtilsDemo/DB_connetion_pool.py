# -*- coding: UTF-8 -*-
import pymysql;
from DBUtils.PooledDB import PooledDB;

import DB_config as Config;

class PTConnectionPool(object):
    __pool = None;

    def getConn(self):
        if self.__pool is None:
            self.__pool = PooledDB(creator=pymysql,
            mincached=Config.DB_MIN_CACHED , 
            maxcached=Config.DB_MAX_CACHED, 
            maxshared=Config.DB_MAX_SHARED,
            maxconnections=Config.DB_MAX_CONNECYIONS, 
            blocking=Config.DB_BLOCKING, 
            maxusage=Config.DB_MAX_USAGE, 
            setsession=Config.DB_SET_SESSION,
            host=Config.DB_TEST_HOST , 
            port=Config.DB_TEST_PORT , 
            user=Config.DB_TEST_USER , 
            passwd=Config.DB_TEST_PASSWORD ,
            db=Config.DB_TEST_DBNAME , 
            use_unicode=False, charset=Config.DB_CHARSET)
            return self.__pool.connection()

    def __enter__(self):
        self.conn = self.getConn()
        self.cursor = self.conn.cursor()
        print "PT数据库创建con和cursor"
        return self

    def __exit__(self, e_t, e_v, t_b):
        self.cursor.close()
        self.conn.close()
        print "PT连接池释放con和cursor"

def getPTConnection():
    return PTConnectionPool()
