import threading, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

value = "hi"

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
    ax = fig.add_subplot(111)
    line, = ax.plot([], [], lw=2, color = "black")
    ax.set_ylim(0, 100)
    ax.set_xlim(0, window)
    ax.grid()
    xdata, ydata = [], []

    def run(data):
        # update the data
        t,y = data
        xdata.append(t)
        ydata.append(y)
        xmin, xmax = ax.get_xlim()

        if t >= xmax:
            ax.set_xlim(xmax, xmax + window)
            ax.figure.canvas.draw()
        line.set_data(xdata, ydata)

        return line,

    ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100,
        repeat=False)
    plt.show()



graphThread = LiveGraph()
graphThread.start()


while 1:

  ops = randint(0, 100)
  time.sleep(0.2)


