import base64
s=base64.encodestring('abc')
print s
ss=base64.decodestring(s)
print ss
