import numpy as np
import pandas as pd
import os
import itertools

table_ranges = pd.read_csv(os.path.join(os.getcwd(), 'Table_Ranges.csv'))
tables_dir = os.path.join(os.getcwd(), 'Raw Tables')
tables = os.listdir(tables_dir)
tables = [os.path.join(tables_dir, table) for table in tables]

t_all = pd.DataFrame()
for idx, row in table_ranges.iterrows():
    print("AA")
    cost_range = np.round(np.arange(row['Cost Min'], row['Cost Max']+1e-4, 1e-4), 5)
    pce_range = np.round(np.arange(row['PCE Min'], row['PCE Max']+0.1, 0.1), 3)
    cost_pce_range = np.asarray(list(itertools.product(cost_range, pce_range)))
    cost_range_p = cost_pce_range[:, 0]
    pce_range_p = cost_pce_range[:, 1]
    t = np.asarray(pd.read_csv(tables[idx])['0'])
    t = np.reshape(t, (len(cost_range), len(pce_range)))
    #t = np.vstack((cost_range_p, pce_range_p, t))
    t = pd.DataFrame(t,columns=pce_range,index=cost_range)
    t_all = pd.concat([t,t_all])
t_all = t_all.sort_index()
t_all.to_csv('Tabulated_LCOE_Main.csv')