#coding:utf-8
from hashlib import sha1
import requests,urllib,json,hmac,base64

openapi="http://openapi.sparta.html5.qq.com"

#demo1
#api="/v3/user/get_info"
#appid='123456'
#appkey="228bf094169a40a3bd188ba37ebe8723&"
#param={'openid':'11111111111111111','openkey':'2222222222222222','appid':appid,'pf':'qzone','format':'json','userip':'112.90.139.30'}

#demo2
api="/v3/pay/buy_goods"
appid="600"
appkey="12345f9a47df4d1eaeb3bad9a7e54321&"
tmp='道具*测试描述信息！！！'
#tmp.decode("gbk").encode("utf-8")
param={'amt':4,'appid':appid,'appmode':1,'format':'json','goodsmeta':tmp,'goodsurl':'http://qzonestyle.gtimg.cn/qzonestyle/act/qzone_app_img/app613_613_75.png','openid':'0000000000000000000000000E111111','openkey':'1111806DC5D1C52150CF405E42222222','payitem':'50005*4*1','pf':'qzone','pfkey':'1B59A5C3D77C7C56D7AFC3E2C823105D','ts':'1333674935','zoneid':'0'}

def paysig(param,api):
    #step 1   urlencode api
    infopath={'':api}
    infopath=urllib.urlencode(infopath)
    infopath=infopath[1:len(infopath)]
    print 'api:'+infopath
    #step 2   dict order by up
    param=sorted(param.iteritems(), key=lambda asd:asd[0], reverse = False)
    print 'source:'+json.dumps(param)
    #step 3   urlencode param and json
    param=urllib.urlencode(param)
    print 'code:'+param
    param="GET&"+infopath+"&"+urllib.quote(param)
    print 'all code:'+param
    return hamcsha1(param,appkey) #substr userInfoApi fist char "="
        
#data sha1 encode
def hamcsha1(data,key):
    sign = hmac.new(key,data, sha1).digest()
    sign = base64.b64encode(sign)
    return sign

#sig=paysig({"amt":4,"appid":600,"appmode":1,"format":"json","goodsmeta":"道具*测试描述信息！！！ ","goodsurl":"http://qzonestyle.gtimg.cn/qzonestyle/act/qzone_app_img/app613_613_75.png","openid":"0000000000000000000000000E111111","openkey":"1111806DC5D1C52150CF405E42222222","payitem":"50005*4*1","pf":"qzone","pfkey":"1B59A5C3D77C7C56D7AFC3E2C823105D","ts":"1333674935","zoneid":0},rechargeApi)
sig=paysig(param,api)
print sig
