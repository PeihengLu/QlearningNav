import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

rewardsEasy = pd.read_excel(os.path.join(os.getcwd(), "rewardsEasy.csv"))
time = rewardsEasy.iloc[:, 0]
reward = rewardsEasy.iloc[:, 1]
d = {'time': time, 'reward': reward}
easy = pd.DataFrame(data=d)
easy = easy[easy.reward == 1]

fig, axs = plt.subplots()
sns.histplot(data=easy.time, binwidth=100, ax=axs)
axs.set_xlim(0, 10000)
axs.set_ylim(0, 30)
fig.savefig('easy.png')

rewardsMedium = pd.read_excel(os.path.join(os.getcwd(), "rewardsMedium.csv"))
time = rewardsMedium.iloc[:, 0]
reward = rewardsMedium.iloc[:, 1]
d = {'time': time, 'reward': reward}
easy = pd.DataFrame(data=d)
easy = easy[easy.reward == 1]

fig, axs = plt.subplots()
sns.histplot(data=easy.time, binwidth=100, ax=axs)
axs.set_xlim(0, 10000)
axs.set_ylim(0, 30)
fig.savefig('medium.png')
