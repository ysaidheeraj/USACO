"""
ID: saidhee1
LANG: PYTHON2
TASK: beads
"""

def get_bead_count(necklace1,break_pt,length):
    i = break_pt
    j = i+1
    cnt = 0
    necklace = list(necklace1)
    color_1 = necklace[i]
    color_2 = necklace[i]
    if i<=length-2:
        color_2 = necklace[j]
    #Assigning color
    if color_1 == 'w':
        while i>=0 and necklace[i] == 'w':
            i-=1
            cnt+=1
        if i >= 0:
            color_1 = necklace[i]
        #i = break_pt
    if color_2 == 'w':
        while j<length and necklace[j] == 'w':
            j+=1
            cnt+=1
    if j<length:
        color_2 = necklace[j]
    while i != j:
        if i== -10000 and j == length+1:
            break
        if i>0 and (necklace[i] == necklace[i-1] and necklace[i] == color_1):
            cnt += 2
            necklace[i] = 'k'
            necklace[i-1] = 'k'
            i -= 2
        elif i>=0 and (necklace[i] == 'w' or necklace[i] == color_1):
            cnt += 1
            necklace[i] = 'k'
            i -= 1
        else:
            i = -10000
        if i == -1:
            i = length - 1
        if j<length-1 and (necklace[j] == necklace[j+1] and necklace[j] == color_2):
            cnt += 2
            necklace[j] = 'k'
            necklace [j+1] = 'k'
            j += 2
        elif j<length and (necklace[j] == 'w' or necklace[j] == color_2):
            cnt += 1
            necklace[j] = 'k'
            j += 1
        else:
            j = length + 1
        if j == length:
            j = 0
    return cnt
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
linelist = fin.readlines()

length = int(linelist[0])
necklace = linelist[1].strip()

#length = input()
#necklace = raw_input()

#necklace += necklace
maximum = 0

for i in range(length):
    break_point = i
    value = get_bead_count(necklace,i,length)
    #print break_point,value
    if value > maximum:
        maximum = value
fout.write(str(maximum)+"\n")
#print maximum