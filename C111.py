import csv
import random
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('studentMarks.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([data],['Math Score'],show_hist=False)
fig.show()

mean=statistics.mean(data)
st=statistics.stdev(data)
print(mean)
print(st)