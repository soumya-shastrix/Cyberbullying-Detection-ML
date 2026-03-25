import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
admission = pd.read_csv('cyberbullying_tweets.csv')
print(admission.head())
print(admission.isnull().sum())
print(admission.shape)
print(admission.index)
print(admission.columns.to_frame().T)
print(admission.count().to_frame().T)
print(admission.info(verbose=True))

x_axis=[1,2,3,4,5,6,7,8,9,10]
findings=[1,1,1,0,0,1,1,0,1,1]
findings1=[0,0,0,1,1,0,0,1,0,0]
fig_size = plt.rcParams["figure.figsize"] #set chart size (longer than taller)
fig_size[0] = 39
fig_size[1] = 10
plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': 18})

plt.stackplot(x_axis, findings, colors=['r'])
plt.stackplot(x_axis, findings1, colors=['g'])

plt.plot([],[],color='r', label='Bully', linewidth=5)
plt.plot([],[],color='g', label='Non-Bully', linewidth=5)
plt.legend()
plt.xlabel('Tweets')
plt.ylabel('Counts')
plt.title("General Statistics of CyberBullying Preprocessed-Dataset")
plt.show()