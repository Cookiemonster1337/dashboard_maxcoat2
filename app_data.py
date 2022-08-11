import pandas as pd

df_tb = pd.read_csv(r'data\dataframes\df_testrig.csv')

tb_voltage = df_tb['AI.U.E.Co.Tb.1 [V]']
tb_temp = df_tb['AI.T.Air.ST.UUT.out [°C]']
tb_hfr = df_tb['HFR [mOhm]'].apply(lambda x: x if x != -99 and x < 100 else None)
tb_j = df_tb['current density [A/cm2]']
timer = df_tb['timer']