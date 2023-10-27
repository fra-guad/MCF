import matplotlib.pyplot as plt
import pandas as pd
mydf=pd.read_csv('4FGL_J2202.7+4216_weekly_9_11_2023.csv')
print(mydf.columns)

ax=mydf['Julian Date']
ay=mydf['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']
plt.xlabel('Julian Date')
plt.ylabel('Photon Flux')
plt.plot(ax,ay)
plt.plot(ax, ay, 'o', color='limegreen')
ey1 =  0.1 * ay

plt.errorbar(ax, ay, yerr=ey1, fmt='o' )
plt.yscale('log')
plt.show()
plt.savefig('file1.png')
