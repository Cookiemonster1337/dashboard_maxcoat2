import pandas as pd
import os


testrig_folder = r'data\testrig'
gamry_folder = r'data\gamry'

# ----------------------------------------------------------------------------------------------------------------------
# FILEIMPORT
# ----------------------------------------------------------------------------------------------------------------------

# CSV - IMPORT
testrig_folder = r'data\testrig'
gamry_folder = r'data\gamry'
tb_dfs = [pd.read_csv(testrig_folder + '/' + f, encoding='cp1252', delimiter='\t', decimal=',') for f in os.listdir(testrig_folder)]

# ----------------------------------------------------------------------------------------------------------------------
# DATAFRAME - TESTBENCH -->tb_df
# ----------------------------------------------------------------------------------------------------------------------

# convert csv do dfs and concat to one dataframe
tb_df = pd.concat(tb_dfs, ignore_index=True)

# manipulate dataframe
tb_df['timer'] = pd.to_datetime(tb_df['Datum / Uhrzeit'], format='%d.%m.%y %H:%M:%S')
tb_df = tb_df.set_index('timer')
starttime = tb_df.index[0]
timer = tb_df.index
tb_df = tb_df.reset_index()
tb_df['current density [A/cm2]'] = round(tb_df['I Summe [A]'] / 25, 2)

tb_df = tb_df[['timer', 'AI.U.E.Co.Tb.1 [V]', 'AI.T.Air.ST.UUT.out [°C]', 'current density [A/cm2]', 'HFR [mOhm]']]

# tb_df.rename(columns={'AI.U.E.Co.Tb.1 [V]':'cell potential [V]', 'AI.T.Air.ST.UUT.out [°C]':'cell temperature [°C]'})

# ----------------------------------------------------------------------------------------------------------------------
# DATAFRAMES - EIS --> eis_dfs
# ----------------------------------------------------------------------------------------------------------------------

eis_files = [f for f in os.listdir(gamry_folder) if 'EIS' in f]

# convert csv to dfs and format columns
columns = ['index', 'datapoints [#]', 'time [s]', 'frequency [Hz]',
          'Z_real [Ohm]', 'Z_imag [Ohm]', 'Z_sig [V]', 'Zmod [ohm]',
          'Z_phz [°C]', 'I_DC [A]', 'V_DC [V]', 'IE_Range [#]']
eis_dfs = [pd.read_csv(gamry_folder + '/' + f, encoding='cp1252',
                       delimiter='\t', decimal=',', skiprows=22, dtype=float,
                       names=columns) for f in eis_files]

# ----------------------------------------------------------------------------------------------------------------------
# DATAFRAMES - CV --> cv1_dfs / cv2_dfs / cv3_dfs / cv4_dfs
# ----------------------------------------------------------------------------------------------------------------------

cv1_files = [f for f in os.listdir(gamry_folder) if 'CV1.1' in f]
# cv2_files = [f for f in os.listdir(gamry_folder) if 'CV1.2' in f]
# cv3_files = [f for f in os.listdir(gamry_folder) if 'CV1.3' in f]
# cv4_files = [f for f in os.listdir(gamry_folder) if 'CV1.4' in f]

# seperate cv-csv by measurement and convert to dfs
cv1_dfs = [pd.read_csv(gamry_folder + '/' + f, encoding='cp1252',
                       delimiter='\t', decimal=',', skiprows=21, dtype=float, usecols=[1, 2, 3]
                      ) for f in cv1_files if 'CV1.1' in f]

# cv2_dfs = [pd.read_csv(gamry_folder + '/' + f, encoding='cp1252',
#                        delimiter='\t', decimal=',', skiprows=21, dtype=float, usecols=[1, 2, 3]
#                       ) for f in cv2_files if 'CV1.2' in f]
#
# cv3_dfs = [pd.read_csv(gamry_folder + '/' + f, encoding='cp1252',
#                        delimiter='\t', decimal=',', skiprows=21, dtype=float, usecols=[1, 2, 3]
#                       ) for f in cv3_files if 'CV1.3' in f]
#
# cv4_dfs = [pd.read_csv(gamry_folder + '/' + f, encoding='cp1252',
#                        delimiter='\t', decimal=',', skiprows=21, dtype=float, usecols=[1, 2, 3]
#                       ) for f in cv4_files if 'CV1.4' in f]

# ----------------------------------------------------------------------------------------------------------------------
# SAVE DATAFRAMES
# ----------------------------------------------------------------------------------------------------------------------

# SAVE DATAFRAME - TESTBENCH
tb_df.to_csv(r'data\dashdata\df_testrig.csv')

# SAVE DATAFRAME - EIS
for i in range(0, len(eis_dfs)):
    name = 'EIS#' + str(i) + '_' + eis_files[i]
    eis_dfs[i].to_csv(r'data\dashdata\'' + name)

# SAVE DATAFRAME - CV
for i in range(0, len(cv1_dfs)):
    name = 'CV#' + str(i) + '_' + cv1_files[i]
    cv1_dfs[i].to_csv(r'data\dashdata\'' + name)

# for i in range(0, len(cv2_dfs)):
#     name = 'CV#' + str(i) + '_' + cv2_files[i]
#     cv2_dfs[i].to_csv(r'data\dashdata\'' + name)
#
# for i in range(0, len(cv3_dfs)):
#     name = 'CV#' + str(i) + '_' + cv3_files[i]
#     cv3_dfs[i].to_csv(r'data\dashdata\'' + name)
#
# for i in range(0, len(cv4_dfs)):
#     name = 'CV#' + str(i) + '_' + cv4_files[i]
#     cv4_dfs[i].to_csv(r'data\dashdata\'' + name)




