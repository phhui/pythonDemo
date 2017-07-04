import requests,urllib,json from hashlib import sha1
import hmac
import base64

openapi="http://openapi.sparta.html5.qq.com"
userInfoApi="/v3/user/get_info"
appid="1106175648"
appkey="umkfea4Ov92xQLpm"
sigkey=appkey+"&"

def getsig(param):
    param=sorted(param.iteritems(), key=lambda asd:asd[0], reverse = False)
    param=urllib.urlencode(param)
    infopath={'':userInfoApi}
    infopath=urllib.urlencode(infopath)
    infopath=infopath[1:len(infopath)]
    print infopath
    param="GET&"+infopath+"&"+urllib.quote(param)
    print "urlencode:"+param
    print 'sigkey:'+sigkey
    return hamcsha1(param,sigkey) #substr userInfoApi fist char "="
    
def hamcsha1(data,key):
    sign = hmac.new(key,data, sha1).digest()
    sign = base64.b64encode(sign)
    print sign
    return sign

def getUserInfo(param):
    param["appid"]=appid
    param["sig"]=getsig(param)
    data=urllib.urlencode(param)
    res=requests.get(openapi+userInfoApi+"?"+data)
    print res.content
    return res.content
getsig({"pf":"qzone","appid":appid,"openkey":"BEA5E8B0D5F2B5872F7ACD00754DEEBE","openid":"13D8F1A4610EC5E0312808F0980EAF93","userip":"117.28.118.24","format":"json"})
