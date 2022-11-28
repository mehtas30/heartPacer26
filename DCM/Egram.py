import time
import matplotlib.pyplot as plt
from matplotlib import animation
# import matplotlib
# matplotlib.use("Qt5Agg")


fig = plt.figure(figsize=(5, 5), dpi=100)
ax = plt.axes(xlim=(0, 10), ylim=(0, 5))
(ln,) = ax.plot([], [], lw=10)
x = [0]
exampleV = [1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 2, 1]
counter = 0  # y counter
gData = [0]


def initGraph():
    ln.set_data([], [])
    return (ln,)


def newStuff(i):
    global ln
    global x
    global exampleV
    global gData
    global counter
    gData.append(exampleV[counter])
    counter = counter + 1
    if counter == 10:
        counter = 0
        # data.pop()
    if len(x) < 10:
        x.append(x[len(x) - 1] + 1)
    else:
        gData.pop(0)
    ln.set_data(x, gData)
    return (ln,)


def graphFunc(type):
    global fig
    global ax
    global ln
    global x
    global exampleV
    global gData
    global counter
    # sleep(1)
    animate = animation.FuncAnimation(
        fig,
        newStuff,
        init_func=initGraph,
        interval=150,
    )
    plt.show()
    print("no")


graphFunc("A")
