import hashlib
m=hashlib.md5()
m.update('phhui')
print m.hexdigest()
