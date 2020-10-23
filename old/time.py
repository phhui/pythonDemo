import time,threading
t=time.time()
lt=int('1706151601')
nt=int(time.strftime('%y%m%d%H%M',time.localtime(time.time())))
#count time
print str(nt-lt)

#ding shi ren wu
dict={'phhui':1}
global timer
def time():
    print str(dict['phhui'])
    dict['phhui']+=1
    timer=threading.Timer(5,time)
    timer.start()
time()
    
