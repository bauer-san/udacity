#https://classroom.udacity.com/courses/cs373-old/lessons/48714404/concepts/486525900923
colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7
p_move = 0.8

numrows = len(colors)
numcols = len(colors[0])

def sense(p, Z):
    q = [[0.0 for i in range(numcols)] for j in range(numrows)]
    s = 0
    pHit = sensor_right

    for i in range(len(p)):
        for j in range(len(p[0])):
            print i,j
            hit = (Z == colors[i][j])
            q[i][j] = (p[i][j] * (hit * pHit + (1-hit) * (1.0-pHit)))

    # normalize
    for i in range(len(p)):
        for j in range(len(p[0])):
            s += q[i][j]

    for i in range(len(p)):
        for j in range(len(p[0])):
            q[i][j] = q[i][j] / s
    return q

def move(p, U):
    q = [0]*len(p)
    for i in range(len(p)):
        idxExact = (i-U)%len(p)
        thisval=p[idxExact]
#        print i, i-1, i+1, thisval
        q[i]     += pExact * thisval
        q[(i-1)%len(p)] += pUndershoot * thisval
        q[(i+1)%len(p)] += pOvershoot * thisval

    return q

def show(p):
    for i in range(len(p)):
        print p[i]

#initialize p
init_p = 1.0 / (numrows * numcols)
p = [[init_p for i in range(numcols)] for j in range(numrows)]

for i in range(len(motions)):
    p = sense(p, measurements[i])
#    p = move(p, motions[i])
    show(p)
