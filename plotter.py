import pandas as pd


testrig_folder = r'data\testrig'
gamry_folder = r'data\gamry'

# FILES TESTRIG

testrig_files = ['maxcoat_ss_coating_#01_20220729.txt',
         'maxcoat_ss_coating_#01_20220730.txt',
         'maxcoat_ss_coating_#01_20220731.txt',
         'maxcoat_ss_coating_#01_20220801.txt',
         'maxcoat_ss_coating_#01_20220802.txt',
         'maxcoat_ss_coating_#01_20220803.txt',
         'maxcoat_ss_coating_#01_20220804.txt',
         'maxcoat_ss_coating_#01_20220805.txt',
         'maxcoat_ss_coating_#01_20220806.txt',
         'maxcoat_ss_coating_#01_20220807.txt',
         'maxcoat_ss_coating_#01_20220808.txt']

dfs = [pd.read_csv(testrig_folder + '/' + f, encoding='cp1252', delimiter='\t', decimal=',') for f in testrig_files]
df = pd.concat(dfs, ignore_index=True)

df['timer'] = pd.to_datetime(df['Datum / Uhrzeit'], format='%d.%m.%y %H:%M:%S')
df = df.set_index('timer')
starttime = df.index[0]
timer = df.index
df = df.reset_index()
df['current density [A/cm2]'] = round(df['I Summe [A]'] / 25, 2)

df.to_csv(r'data\dataframes\df_testrig.csv')

voltage = df['AI.U.E.Co.Tb.1 [V]']
temperature = df['AI.T.Air.ST.UUT.out [°C]']
hfr = df['HFR [mOhm]'].apply(lambda x: x if x != -99 and x < 100 else None)
current_density = df['current density [A/cm2]']


