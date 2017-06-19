import json
dict={'phhui':{'key':'xxxxx'},'56lea':'abcdef'}
print json.dumps(dict)
print dict['phhui'].get('key')
print len(dict)>1 and True or False

for i in dict:
    print str(i)
    print dict[i]

dict['phhui']=None

if dict['phhui']:
    print dict['phhui']
else :
    print 'null'

if dict.get('56lea'):
    print dict['56lea']
else :
    print 'no'
