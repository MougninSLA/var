#!/usr/bin/env python3

f = open('/var/www/scripts/test')
li = []
for ln in f:
	li.append(ln)
f.close()

del(li[:3])

li2 = []
for i in li:
	i = i.split()
	li2.append(i[6]+" "+i[5])
h = {}
while li2:
	a = li2.count(li2[0])
	h[li2[0]] = a
	i = li2[0]
	li2 = [y for y in li2 if y != i]
v = sorted(h)
print(h)
