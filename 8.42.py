## -*- coding: utf-8 -*-
#"""
#Created on Wed Apr  3 18:23:59 2019
#
#@author: Lenovo
#"""
#import numpy as np
#from matplotlib.pyplot import*
#from matplotlib.animation import FuncAnimation
ns=40;np1=10000;xL=0;xR=1;yL=0;yR=1
def init():
        m=int(sqrt(np1))
        s=0.1
        a=np.linspace(xL,xR/2,m)
        b=np.linspace(yL,yR,m)
        xpositions=[]
        ypositions=[]
        for i in a:
                for j in b:
                      xpositions.append(round(i,2))
                      ypositions.append(round(j,2))
        xpositions=np.array(xpositions)
        ypositions=np.array(ypositions)
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import seaborn

fig, ax = plt.subplots()

x = np.arange(0, 20, .01)
ax.scatter(x, x+np.random.normal(0, 3, len(x)))
line, = ax.plot(x, x-5, 'r-', lw=2)


# i => ith frame
def update(i):
    line.set_ydata(x-5+i)
    ax.set_xlabel('frame {0}'.format(i))
    return line, ax

if __name__ == '__main__':

    animation = FuncAnimation(fig, update, frames=np.arange(0, 20), interval=200)
        # 200ms 的间隔，相当于 5fps，一秒 5 帧
    plt.show()
