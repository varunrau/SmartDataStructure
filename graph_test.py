import threading, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

class LiveGraph(threading.Thread):
  def run(self):

    window = 20

    def data_gen():
        t = data_gen.t
        while 1:
            t += 0.1
            yield t, ops
    data_gen.t = 0

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    line, = ax1.plot([], [], lw=2, color = "black")
    ax1.set_ylim(0, 100)
    ax1.set_xlim(0, window)
    ax1.grid()

    xdata, ydata = [], []

    def run(data):
        # update the data
        t,y = data
        xdata.append(t)
        ydata.append(y)
        xmin, xmax1 = ax1.get_xlim()

        if t >= xmax1:
            ax1.set_xlim(xmax1, xmax1 + window)
            ax1.figure.canvas.draw()
        line.set_data(xdata, ydata)

        return line,

    ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100,
        repeat=False)
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


