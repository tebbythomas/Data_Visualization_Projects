'''
Description:
Program to plot real time data as line plots. We are plotting real time
Youtube subscriber count data
'''
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []


index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    # Clear axis
    plt.cla()
    plt.plot(x, y1, label="Channel 1")
    plt.plot(x, y2, label="Channel 2")
    plt.legend(loc='upper left')
    plt.title('Youtube Channel Subscriber Count Live Data')
    plt.xlabel('Time in (s)')
    plt.ylabel('Subscriber Count')
    plt.savefig('real_time.png')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.savefig('real_time.png')
plt.show()
