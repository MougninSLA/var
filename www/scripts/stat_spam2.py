#!/usr/bin/env python3

f = open('/var/www/scripts/test2')
li = []
for ln in f:
	li.append(ln)
f.close()

del(li[:3])

li2 = []
for i in li:
	i = i.split()
	li2.append(i[5])
h = {}
while li2:
	a = li2.count(li2[0])
	h[li2[0]] = a
	i = li2[0]
	li2 = [y for y in li2 if y != i]
v = sorted(h)
print(h)

for g in v:
	for key in h.keys():
		if g == key:
			print("Le ",key,", il y a eu ",h[key])

print("==============================================================\n")

lim = []
for i in li:
	i = i.split()
	y = i[5].split("-")
	del(y[2])
	y = "-".join(y)
	lim.append(y)

s = {}
while lim:
	a = lim.count(lim[0])
	s[lim[0]] = a
	i = lim[0]
	lim = [y for y in lim if y != i]
v = sorted(s)

for g in v:
	for key in s.keys():
		if g == key:
			print("Le ",key,", il y a eu ",s[key])

print("==============================================================\n")

lia = []
for i in li:
        i = i.split()
        y = i[5].split("-")
        del(y[-2:])
        y = "".join(y)
        lia.append(y)

z = {}
while lia:
        a = lia.count(lia[0])
        z[lia[0]] = a
        i = lia[0]
        lia = [y for y in lia if y != i]
v = sorted(z)

for g in v:
	for key in z.keys():
		if g == key:
			print("Le ",key,", il y a eu ",z[key])