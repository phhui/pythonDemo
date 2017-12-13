#coding=utf-8
import requests
import sys
import time
import thread
import httplib, urllib
import random
import uuid
import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='测试脚本日志.log',
                filemode='w')

def log_uncaught_exceptions(exception_type, exception, tb):
    logging.critical(''.join(traceback.format_tb(tb)))
    logging.critical('{0}: {1}'.format(exception_type, exception))
sys.excepthook = log_uncaught_exceptions

#网关地址
addr="119.29.150.22"
port=8086
thread_count = 150 #单次并发数量
requst_interval = 10 #请求间隔(秒)
test_count = sys.maxsize #sys.maxsize  # 指定测试次数


#字段说明,必须一一对应
#login为空表示使用随机用户名

user_list=["phhui","papa","pq01","pq02","pq03","pq04","pq05","pq06","pq07","pq08","pq09","pq10"]

now_count = 0
lock_obj = thread.allocate()
def send_http():
    global now_count
    try:
        for user in user_list:
	    print user
	    res=requests.post("http://119.29.150.22:8086/login",data={"openid":user})
            print '发送数据: ' + user
            print '返回数据: ' + res[0,10]

            logging.info('发送数据: ' + user)
#            logging.info('返回数据: ' + res.content)
            #print response.getheaders() #获取头信息
            sys.stdout.flush()
            now_count+=1
    except Exception, e:
        print e
        logging.info(e)

def test_func(run_count):
    global now_count
    global requst_interval
    global lock_obj
    cnt = 0
    while cnt < run_count:
        lock_obj.acquire()
        print ''
        print '***************************请求次数:' + str(now_count) + '*******************************'
        print 'Thread:(%d) Time:%s\n'%(thread.get_ident(), time.ctime())

        logging.info(' ')
        logging.info('***************************请求次数:' + str(now_count) + '*******************************')
        logging.info('Thread:(%d) Time:%s\n'%(thread.get_ident(), time.ctime()))
        cnt+=1
        send_http()
        sys.stdout.flush()
        lock_obj.release()
        time.sleep(requst_interval)

def test(ct):
    global thread_count
    for i in range(thread_count):
        thread.start_new_thread(test_func,(ct,))

if __name__=='__main__':
    global test_count
    test(test_count)
    while True:
        time.sleep(100)
