'''
Reference:
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

Description:
Bar chart to plot most popular programming languages used by developers in a
survey conducted by StackOverflow
'''
import csv
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd


plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))
languages = list()
popularity = list()
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)


plt.title('Most Popular Languages')
plt.xlabel('Number of Developers who use')

plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()
