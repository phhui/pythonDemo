import urllib
data={'':'/v3/user/get_info','openid':"abc",'openkey':"openkey",'appid':"123",'appkey':"321",'pf':"qzone"}
data=sorted(data.iteritems(), key=lambda asd:asd[0], reverse = False)
sig=urllib.urlencode(data)
print sig
sig=urllib.unquote(sig)
print sig
sig=urllib.quote(sig)
print sig

url='/v3/user/get_info%='
ui={'':url}
ui=urllib.urlencode(ui)
ui=ui[1:len(ui)]
print ui

uj=urllib.quote(url)
print uj.replace('/','%2f')

st="amt=500&appid=1106175648&appmode=1&format=json&goodsmeta=%E5%85%83%E5%AE%9D%2A%E7%94%A8%E4%BA%8E%E8%B4%AD%E4%B9%B0%E5%95%86%E5%9F%8E%E7%89%A9%E5%93%81&goodsurl=http%3A%2F%2Fs23.app1106175648.qqopenapp.com%2Fassets%2Fimg%2Fyb.png&openid=13D8F1A4610EC5E0312808F0980EAF93&openkey=B511FA1980D37CF3F8BF0176CE3DC5E8&payitem=1000%2A10%2A50&pf=qzone&pfkey=44a1c46814a064d31559a1386e743d31&ts=1499416609&zoneid=0"
st=st.replace("=","%3D")
print st
