import urllib
data={'':'/v3/user/get_info','openid':"abc",'openkey':"openkey",'appid':"123",'appkey':"321",'pf':"qzone"}
data=sorted(data.iteritems(), key=lambda asd:asd[0], reverse = False)
sig=urllib.urlencode(data)
print sig
