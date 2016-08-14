#Modify the move function to accommodate the added
#probabilities of overshooting or undershooting
#the intended destination.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

global p
p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
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

def update():
	p= move(p, 1)
	plt.bar([0,1,2,3,4],p)
	return p

#fig=plt.figure()

#animation.FuncAnimation(fig, update, frames=10, init_func=None, fargs=None, save_count=None)

#print p




