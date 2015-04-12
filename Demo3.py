#coding=utf-8
u = u'汉'
print repr(u)
s = u.encode('UTF-8')
print repr(s)
u2 = s.decode('UTF-8')
print repr(u2)