"""
ID: saidhee1
LANG: PYTHON2
PROG: ride
"""

def get_product(name):
	product = 1
	for char in name:
		product *= ((ord(char)-ord('A'))+1)
	return product

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
linelist = fin.readlines()
cometname = linelist[0]
groupname = linelist[1]

cometproduct = get_product(cometname)
groupproduct = get_product(groupname)
print cometproduct,groupproduct

if cometproduct%47 == groupproduct%47:
	fout.write("GO\n")
else:
	fout.write("STAY\n")