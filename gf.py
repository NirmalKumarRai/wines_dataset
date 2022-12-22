import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df = pd.DataFrame({'day':[1,2,3,4,5],'visitors':[200,302,480,590,680],'Bounce_rate':[20,30,40,50,60]})
df.set_index('day',inplace=True)

df.plot()
plt.show()