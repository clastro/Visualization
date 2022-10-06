import matplotlib.pyplot as plt
import pandas as pd

plt.scatter(df_scatter2[(df_scatter2.true == 0)].index,df_scatter2['probability'][(df_scatter2.true == 0)],
           marker='D',
           color='blue',
           label='Normal',s=0.5) #scatter 1
           
plt.scatter(df_scatter2[(df_scatter2.true == 1)].index,df_scatter2['probability'][(df_scatter2.true == 1)],
           marker='o',
           color='red',
           label='AFib',s=0.5) #scatter 2
           
plt.plot([0, 10753], [0.85, 0.85], 'k-', color = 'green', label = 'cut off(upper) = 0.85') # Line 1 ( y=0.85 )
plt.plot([0, 10753], [0.1, 0.1], 'k-', color = 'yellow', label = 'cut off(lower) = 0.1') # Line 2 ( y = 0.1 )

plt.xlabel('sample') # X-axis
plt.ylabel('Probability') # y-axis
plt.legend(loc='upper left') # Label explanation
plt.show() #show plot
