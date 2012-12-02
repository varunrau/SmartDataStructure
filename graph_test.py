import threading, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint
from DS import *

class LiveGraph(threading.Thread):
  def run(self):
    
    #initialization code to make graph look pretty
    window = 20
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.6)#more height between subplots
    fig.set_facecolor("#FFFFFF")
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    

    line, = ax1.plot([], [], lw=3, color = "black")
    x = [0,4]
    n, bins, patches = ax2.hist(x, 4, normed=False, facecolor='green', rwidth = 0.95, alpha=0.75)
    
    ax1.set_ylim(0, 100)
    ax1.set_xlim(0, window)
    ax1.grid()
    
    ax2.set_ylim(0, 100)
    #ax2.set_xlim(0, window)
    ax2.yaxis.grid()
    labels = ["get","add","remove","contains"]
    ax2.set_xticks(bins)
    ax2.xaxis.set_visible(False);
    
    # Label operation names below x-axis
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]
    for x, label in zip(bin_centers, labels):
        ax2.annotate(label, xy=(x, 0), xycoords=('data', 'axes fraction'), xytext=(0, -18), textcoords='offset points', va='top', ha='center')    
    
    xdata, ydata = [], []

    # Update graph variables that change over time
    def data_gen():
        t = data_gen.t
        while 1:
            t += 0.1
            yield t, ops, get, add, remove, contains
    data_gen.t = 0



    def run(data):
        # update line graph (ops/sec)
        t,y, get, add, remove, contains = data
        xdata.append(t)
        ydata.append(y)
        xmin1, xmax1 = ax1.get_xlim()
        ymin1, ymax1 = ax1.get_ylim()

        if t >= xmax1:
            ax1.set_xlim(xmax1, xmax1 + window)
            ax1.figure.canvas.draw()
        
        if y >= ymax1:
            ax1.set_ylim(ymin1, ymax1 * 1.5)
            ax1.figure.canvas.draw()
        line.set_data(xdata, ydata)
        
        # update bar graph (freqency per op)
        ymin2, ymax2 = ax2.get_ylim()
        operations = [get, add, remove, contains]
        
        for i in range(4):
          patches[i].set_height(operations[i])
          if operations[i] >= ymax2:
            ax2.set_ylim(ymin2, ymax2 * 1.5)
            ax2.figure.canvas.draw()

        return line, patches

    ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100,
        repeat=False)
        
    plt.subplots_adjust(bottom=0.15)
    plt.show()



graphThread = LiveGraph()
graphThread.start()


while 1:

  ops = randint(0, 100)
  get = randint(0, 100)
  add = randint(0, 100)
  remove = randint(0, 100)
  contains = randint(0, 100)
  time.sleep(0.2)


