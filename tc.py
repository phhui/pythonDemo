#coding:utf-8
import requests,urllib,json
from hashlib import sha1
import hmac,base64,time,json,copy

openapi="http://openapi.sparta.html5.qq.com"
userInfoApi="/v3/user/get_info"
checkLogin="/v3/user/is_login"
rechargeApi="/v3/pay/buy_goods"
appid="1106175648"
#appkey="umkfea4Ov92xQLpm"
appkey="12345f9a47df4d1eaeb3bad9a7e54321"
sigkey=appkey+"&"

#get tencent sig key
def get_sig(self,param,api):
    if param.get("pfkey"):
        param.pop('pfkey')
    param=sorted(param.iteritems(), key=lambda asd:asd[0], reverse = False)
    param=urllib.urlencode(param)
    infopath={'':api}
    infopath=urllib.urlencode(infopath)
    infopath=infopath[1:len(infopath)]
    param="GET&"+infopath+"&"+urllib.quote(param)
    return self.hamcsha1(param,self.sigkey) #substr userInfoApi fist char "="

def paysig(param,api):
    param=sorted(param.iteritems(), key=lambda asd:asd[0], reverse = False)
    print 'source:'+json.dumps(param)
    param=urllib.urlencode(param)
    print 'code:'+param
    infopath={'':api}
    infopath=urllib.urlencode(infopath)
    infopath=infopath[1:len(infopath)]
    param="GET&"+infopath+"&"+urllib.quote(param)
    print 'all code:'+param
    return hamcsha1(param,sigkey) #substr userInfoApi fist char "="
        
#data sha1 encode
def hamcsha1(data,key):
    sign = hmac.new(key,data, sha1).digest()
    sign = base64.b64encode(sign)
    return sign

sig=paysig({"amt":4,"appid":600,"appmode":1,"format":"json","goodsmeta":"道具*测试描述信息！！！ ","goodsurl":"http://qzonestyle.gtimg.cn/qzonestyle/act/qzone_app_img/app613_613_75.png","openid":"0000000000000000000000000E111111","openkey":"1111806DC5D1C52150CF405E42222222","payitem":"50005*4*1","pf":"qzone","pfkey":"1B59A5C3D77C7C56D7AFC3E2C823105D","ts":"1333674935","zoneid":0},rechargeApi)
print sig
