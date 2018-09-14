"""
ID: saidhee1
LANG: PYTHON2
TASK: transform
"""

def vertical_reflection(matrix):
    n = len(matrix)
    reflected = []
    for i in range(n):
        j = n-1
        row = []
        while j>=0:
            row.append(matrix[i][j])
            j -= 1
        reflected.append(row)
    return reflected

def rotate_90(original,answer):
    rotated = []
    n = len(original)
    for i in range(n):
        row = []
        for j in range(n):
            row.append(original[j][i])
        rotated.append(row)
    new_rotated = vertical_reflection(rotated)
    return new_rotated
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
linelist = fin.readlines()

def verify_rotations(original,rotated,output):
    
    new_rotated = rotate_90(original,rotated)
    if new_rotated == rotated:
        if output == 1:
            fout.write("5\n")
        else:    
            fout.write("1\n")
        return 1
    else:
        new_rotated = rotate_90(new_rotated,rotated)
        if new_rotated == rotated:
            if output == 1:
                fout.write("5\n")
            else:
                fout.write("2\n")
            return 1
        else:
            new_rotated = rotate_90(new_rotated,rotated)
            if new_rotated == rotated:
                if output == 1:
                    fout.write("5\n")
                else:
                    fout.write("3\n")
                return 1
    return 0

n = int(linelist[0])
original = []
rotated = []

m = n*2
j = 1
for i in range(1,n+1):
    line = linelist[i]
    line_chars = list(line.strip())
    row = []
    for char in line_chars:
        row.append(char)
    original.append(row)

j = 1
for i in range(n+1,m+1):
    line = linelist[i]
    line_chars = list(line.strip())
    row = []
    for char in line_chars:
        row.append(char)
    rotated.append(row)


flag = verify_rotations(original,rotated,0)

vertical = vertical_reflection(original)
if not flag:
    if vertical == rotated:
        fout.write("4\n")
    else:
        if not flag:
            flag = verify_rotations(vertical,rotated,1)
            if original == rotated:
                fout.write('6'+"\n")
            if not flag:
                fout.write(str("7\n"))


