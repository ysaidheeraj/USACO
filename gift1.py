"""
ID: saidhee1
LANG: PYTHON2
TASK: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
linelist = fin.readlines()
friend_money={}
no_of_friends = int(linelist[0])
length = len(linelist)
i=1
while i<length:
    while i<=no_of_friends:
        friend_money[linelist[i].strip()] = 0
        i+=1

    if i == no_of_friends+1:
        while i<length:
            string = linelist[i].strip()
            i+=1
            amt,no = map(int,linelist[i].split())
            amt=amt*(-1)
            i+=1

            try:
                divided = abs(amt)/no
            except ZeroDivisionError:
                divided = 0
            original_s = abs(amt) - (no*divided)
            friend_money[string] += original_s + amt

            while no>0:
                friend_money[linelist[i].strip()] += divided
                i+=1
                no-=1

i =1
while i<=no_of_friends:
    fout.write(linelist[i].strip()+" "+str(friend_money[linelist[i].strip()])+"\n")
    i+=1