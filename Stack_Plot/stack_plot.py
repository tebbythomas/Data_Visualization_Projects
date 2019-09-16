'''
Description:
Stack plot depicting number of hours each employee spent on a project
'''

from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


days = [1, 2, 3, 4, 5, 6, 7, 8, 9]

emp1_hours = [8, 6, 5, 5, 4, 2, 1, 1, 0]
emp2_hours = [0, 1, 2, 2, 2, 4, 4, 4, 4]
emp3_hours = [0, 1, 1, 1, 2, 2, 3, 3, 4]


labels = ['Employee1', 'Employee2', 'Employee3']
colors = ['#6d904f', '#fc4f30', '#008fd5']
plt.stackplot(days, emp1_hours, emp2_hours, emp3_hours, labels=labels, colors=colors)

plt.title("Employee Hours on Project")
plt.legend(loc=(0.07, 0.05))
plt.tight_layout()
plt.savefig('stack_plot.png')
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
