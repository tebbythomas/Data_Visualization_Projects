'''
Reference:
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
'''
from matplotlib import pyplot as plt
import numpy as np


plt.style.use('ggplot')

# Ages
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes, py_dev_y, width=width, color='#008fd5', label='Python Devs')


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, js_dev_y, width=width, color='#e5ae38', label='Javascript Devs')


plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.xticks(ticks=x_indexes, labels=ages_x)
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()
