import threading
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import globalz
from DS import *
lastNumOps = 0
lastDS = -1
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
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("#Data Structure Operations")
    ax1.grid()

    
    ax2.set_ylim(0, 100)
    #ax2.set_xlim(0, window)
    ax2.yaxis.grid()
    labels = ["contains","add","remove","get"]
    ax2.set_xticks(bins)
    ax2.xaxis.set_visible(False);
    ax2.set_ylabel("Frequency of Data Structure Operations");
    
    # Label operation names below x-axis
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]
    for x, label in zip(bin_centers, labels):
        ax2.annotate(label, xy=(x, 0), xycoords=('data', 'axes fraction'), xytext=(0, -18), textcoords='offset points', va='top', ha='center')    
    
    xdata, ydata = [], []
    
    # Update graph variables that change over time
    def get_data():
      t = get_data.t
      while 1:
          t += 0.1
          yield t, globalz.num_ops, globalz.which, globalz.contains_ctr, globalz.add_ctr, globalz.remove_ctr, globalz.get_ctr
    get_data.t = 0


    
    def update(data):
        global lastNumOps
        global lastDS
        # update line graph (ops/sec)
        t,ops, which, contains, add, remove, get = data
        opsPerSec = ops - lastNumOps
        lastNumOps = ops
        
        xdata.append(t)
        ydata.append(opsPerSec)
        xmin1, xmax1 = ax1.get_xlim()
        ymin1, ymax1 = ax1.get_ylim()

        if t >= xmax1:
            ax1.set_xlim(xmax1, xmax1 + window)
            ax1.figure.canvas.draw()
        
        if opsPerSec >= ymax1:
            ax1.set_ylim(ymin1, ymax1 * 1.5)
            ax1.figure.canvas.draw()
        
        line.set_data(xdata, ydata)
        
        # Draw red circle when data structure changes
        if lastDS != which:
          ax1.scatter(xdata[len(xdata)-1],ydata[len(ydata)-1],s=50,color="red")
          lastDS = which
        
        plt.title(DS.STRINGS[which], color="#000000")  
          
        # update bar graph (freqency per op)
        ymin2, ymax2 = ax2.get_ylim()
        operations = [contains, add, remove, get]
        
        for i in range(4):
          patches[i].set_height(operations[i])
          if operations[i] >= ymax2:
            ax2.set_ylim(ymin2, ymax2 * 1.5)
            ax2.figure.canvas.draw()

        return line, patches

    ani = animation.FuncAnimation(fig, update, get_data, blit=False, interval=100,
        repeat=False)
        
    plt.subplots_adjust(bottom=0.15)
    plt.show()
