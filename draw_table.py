import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import pandas as pd

data = pd.read_csv('Tabulated_LCOE_Main.csv',index_col=0)
Cost = np.asarray(data.index.values)
PCE = np.asarray(data.columns.values).astype(float)
PCE = np.around(PCE, 1)
LCOE = np.asarray(data.values)
xx,yy = np.meshgrid(Cost, PCE)
plt.pcolormesh(Cost, PCE, LCOE.T, norm=colors.LogNorm(vmin=LCOE.min() , vmax=1e2), cmap='inferno')
plt.colorbar(label='LCOE ($/kWh)')
CS = plt.contour(Cost, PCE, LCOE.T, [0.02,0.04,0.06,0.08,0.1,0.2], colors='white',)
plt.clabel(CS, inline=True, fontsize=10)
plt.xlabel('Cost ($)')
plt.ylabel('PCE (%)')
plt.savefig('Tabulated_LCOE.png',dpi=1200)