"""
ID: saidhee1
LANG: PYTHON2
TASK: milk2
"""

fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
linelist = fin.readlines()


durations = set()
N = int(linelist[0])

for i in range(1,N+1):
    s,e = map(int,linelist[i].split())
    durations.update(range(s,e))

start,end = min(durations),max(durations)
presence = [int(i in durations) for i in range(start,end+1)]

string = ''.join(list(map(str,presence)))

busy = len(max(string.split('0'), key = len))
idle = len(max(string.split('1'),key = len))
fout.write(str(busy)+" "+str(idle)+"\n")