from sql import *
import json
res=sqlHelper.update("insert into l_user (l_uid,l_name) values(%s,%s)",("' or 1=1'",'alctlc'))
print json.dumps(res)
