import matplotlib.pyplot as plt
from matplotlib import animation
import time

# def Egram(serialRead=None):

#     a = serialRead()

#     axs[0].cla()
#     axs[0].set_yticks([-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -
#                       1, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
#     axs[0].set_y
#     o, (-5, 5)
#     axs[0].grid()
#     axs[0].set_ylabel("Amplitude(mV)")
#     axs[0].plot(x, a, c='g', label='Artial', linewidth=3.0)
#     axs[0].set_title('Atrial')

#     axs[1].cla()
#     axs[1].set_yticks([-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -
#                       1, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
#     axs[1].set_ylim(-5, 5)
#     axs[1].grid()
#     axs[1].set_xlabel("Time(msec)")
#     axs[1].set_ylabel("Amplitude(mV)")
#     axs[1].plot(x, a, c='r', label='Ventricular', linewidth=3.0)
#     axs[1].set_title('Ventricular')

#     axs[2].cla()
#     axs[2].set_yticks([-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -
#                       1, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
#     axs[2].set_ylim(-5, 5)
#     axs[2].grid()
#     axs[2].set_xlabel("Time(msec)")
#     axs[2].set_ylabel("Amplitude(mV)")
#     axs[2].plot(x, a, c='g', label='Artial', linewidth=3.0)
#     axs[2].plot(x, a, c='r', label='Ventricular', linewidth=3.0)
#     axs[2].set_title('Artial & Ventricular')


# fig, axs = plt.subplots(2)
# animate = animation.FuncAnimation(fig, interval=150)
# plt.show()
fig = plt.figure()
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


def graph(type):
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


# graphA()
