import json
dict={'phhui':{'key':'xxxxx'},'56lea':'abcdef'}
print dict.get('phhuib')
if dict.get('phhuib')==False:
    print 'aa'
else :
    print 'bb'

def reqtest(param):
    if param==1:
        return {'name':'txw'}
    elif param==2:
        return True
    else:
        return False
print reqtest(1)
print reqtest(2)
print reqtest(3)

def abc():
    return 'ok' if reqtest(1) else reqtest(2)
print abc()
