import csv
import random
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('studentMarks.csv')
data=df['Math_score'].tolist()

def randomSetOfMean(counter):
    dataset=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    sd=statistics.stdev(dataset)
    return mean

meanlist=[]
for i in range(0,1000):
    setOfMean=randomSetOfMean(100)
    meanlist.append(setOfMean)

fmean=statistics.mean(meanlist)
fst=statistics.stdev(meanlist)
print(fmean)
print(fst)

firstsdstart,firstsdend=fmean-fst,fmean+fst
secondsdstart,secondsdend=fmean-2*fst,fmean+2*fst
thirdsdstart,thirdsdend=fmean-3*fst,fmean+3*fst
print(firstsdstart,firstsdend)
print(secondsdstart,secondsdend)
print(thirdsdstart,thirdsdend)


fig=ff.create_distplot([meanlist],['Math Score'],show_hist=False)
fig.add_trace(go.Scatter(x=[fmean,fmean],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[firstsdstart,firstsdstart],y=[0,0.17],mode='lines',name='sd1start'))
fig.add_trace(go.Scatter(x=[firstsdend,firstsdend],y=[0,0.17],mode='lines',name='sd1end'))
fig.add_trace(go.Scatter(x=[secondsdstart,secondsdstart],y=[0,0.17],mode='lines',name='sd2start'))
fig.add_trace(go.Scatter(x=[secondsdend,secondsdend],y=[0,0.17],mode='lines',name='sd2end'))
fig.add_trace(go.Scatter(x=[thirdsdstart,thirdsdstart],y=[0,0.17],mode='lines',name='sd3start'))
fig.add_trace(go.Scatter(x=[thirdsdend,thirdsdend],y=[0,0.17],mode='lines',name='sd3end'))

fig.show()

