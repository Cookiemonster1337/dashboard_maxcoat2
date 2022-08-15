import pandas as pd
import os

datafolder = r'data\dashdata'

# GRAPHDATA - TESTBENCH
df_tb = pd.read_csv(datafolder + '/df_testrig.csv')

tb_voltage = df_tb['AI.U.E.Co.Tb.1 [V]']
tb_temp = df_tb['AI.T.Air.ST.UUT.out [°C]']
tb_hfr = df_tb['HFR [mOhm]'].apply(lambda x: x if x != -99 and x < 100 else None)
tb_j = df_tb['current density [A/cm2]']
timer = df_tb['timer']

# GRAPHDATA - EIS
dfs_eis = [pd.read_csv(datafolder + '/' + f) for f in os.listdir(datafolder) if 'EIS' in f]

# GRAPHDATA - CV
dfs_cv1 = [pd.read_csv(datafolder + '/' + f) for f in os.listdir(datafolder) if 'CV1.1' in f]
