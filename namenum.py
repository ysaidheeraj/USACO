"""
ID: saidhee1
LANG: PYTHON2
TASK: namenum
"""

fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')
test_data = open('dict.txt','r')
linelist = fin.readlines()
names = [name.strip() for name in test_data.readlines()]

num = [int(i) for i in linelist[0].strip()]

num_map = {2: ['A','B','C'],3:['D','E','F'],4: ['G','H','I'],5: ['J','K','L'],6: ['M','N','O'],7: ['P','R','S'],8: ['T','U','V'],9: ['W','X','Y']  }

length = len(num)
count = 0
for name in names:
    l =len(name)
    if name[0] in num_map[num[0]] and length == l:
        name = name.upper()
        flag = 0
        for i in range(l):
            if  name[i] not in num_map[num[i]]:
                flag = 1
                break
        if flag == 0:
            count += 1
            fout.write(name+"\n")
if count == 0:
    fout.write("NONE\n")