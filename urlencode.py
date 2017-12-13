import urllib
data={'':'/v3/user/get_info','openid':"abc",'openkey':"openkey",'appid':"123",'appkey':"321",'pf':"qzone"}
data=sorted(data.iteritems(), key=lambda asd:asd[0], reverse = False)
sig=urllib.urlencode(data)
sig=urllib.quote(sig)
#print sig

url='/v3/user/get_%info=xx'
ui={'':url}
ui=urllib.urlencode(ui)
ui=ui[1:len(ui)]
print ui

uj=urllib.quote(url)
print uj

uk=urllib.quote_plus(url)
print uk

