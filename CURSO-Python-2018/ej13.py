# 

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
#np.random.seed(19680801)

# fake up some data
#spread = np.random.rand(50) * 100
#center = np.ones(25) * 50
#flier_high = np.random.rand(10) * 100 + 100
#flier_low = np.random.rand(10) * -100
#data = np.concatenate((spread, center, flier_high, flier_low))
fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')

data=[
	[1,2,3,4,5,6,6,6,6,6],
	[3,4,5,6,7,7,7,5,4,4],
	[3,4,5,6,7,7,7,5,4,4],
	[3,4,5,6,7,7,7,5,4,4],
	[3,4,5,6,7,7,7,5,4,4],
]

ax1.boxplot(data,labels=[
	'aa',
	'zdd',
	'eds',
	'dsd',
	'fsd',
	])

plt.show()