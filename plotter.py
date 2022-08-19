import pandas as pd
import os
pd.options.mode.chained_assignment = None  # default='warn'


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
df_tb = pd.concat(tb_dfs, ignore_index=True)

# manipulate dataframe
df_tb['timer'] = pd.to_datetime(df_tb['Datum / Uhrzeit'], format='%d.%m.%y %H:%M:%S')
df_tb = df_tb.set_index('timer')
starttime = df_tb.index[0]
timer = df_tb.index
df_tb = df_tb.reset_index()
df_tb['current density [A/cm2]'] = round(df_tb['I Summe [A]'] / 25, 2)
df_tb['mean current density [A/cm2]'] = 0
df_tb['ASR [mOhm*cm2]'] = 0
df_tb['duration [s]'] = 0


comment_marker = ''
start_marker = 0
for i in range(0, len(df_tb)):
    if df_tb['HFR [mOhm]'][i] > 0:
        df_tb['ASR [mOhm*cm2]'][i] = df_tb['HFR [mOhm]'][i] * 25
    else:
        df_tb['ASR [mOhm*cm2]'][i] = None
    if df_tb['Kommentar'][i] != comment_marker:
        comment_marker = df_tb['Kommentar'][i]
        df_tb['mean current density [A/cm2]'][start_marker:i-1] = \
            df_tb['current density [A/cm2]'][start_marker:i-1].mean()
        start_marker = i


df_tb_comp = df_tb

df_tb = df_tb[(df_tb['timer'] <= '2022-07-30 13:45:00') | (df_tb['timer'] >= '2022-08-02 10:15:00')]
df_tb = df_tb.reset_index()
df_tb['time'] = pd.to_datetime(df_tb['timer'], format='%Y-%m-%d %H:%M:%S')

gap = 10094
start = df_tb['time'][0]
start2 = df_tb['time'][gap]

for i in range(1, len(df_tb)):
    if i < gap:
        df_tb['duration [s]'][i] = (df_tb['time'][i] - start).total_seconds()
        duration = df_tb['duration [s]'][i]
    else:
        df_tb['duration [s]'][i] = ((df_tb['time'][i] - start2).total_seconds()) + duration

df_tb = df_tb[['timer', 'duration [s]', 'AI.U.E.Co.Tb.1 [V]', 'AI.T.Air.ST.UUT.out [°C]', 'current density [A/cm2]',
               'HFR [mOhm]']]

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
df_tb.to_csv(r'data\dashdata\df_testrig.csv')

# SAVE DATAFRAMES - IV
iv_markers = df_tb_comp.index[df_tb_comp['Kommentar'] == '#IV-CURVE#'].tolist()


for i in range(0, len(iv_markers)):

    if i == len(iv_markers) - 1:
        df_iv = df_tb_comp.iloc[iv_markers[i]:]
    else:
        df_iv = df_tb_comp.iloc[iv_markers[i]: iv_markers[i + 1]]

    name = 'POL#' + str(i) + '_' + df_iv['Datum / Uhrzeit'][iv_markers[i]][:8]

    df_iv = df_iv[df_iv['Kommentar'] == 'ui1_messen']
    df_iv = df_iv[df_iv['current density [A/cm2]'] != 1.19]

    df_iv = df_iv[['timer', 'AI.U.E.Co.Tb.1 [V]', 'AI.T.Air.ST.UUT.out [°C]', 'current density [A/cm2]', 'HFR [mOhm]',
                   'mean current density [A/cm2]']]

    df_iv.to_csv(r'data\dashdata' + '/' + name)



# SAVE DATAFRAMES - AST
ast_markers = df_tb_comp.index[df_tb_comp['Kommentar'] == '#AST-CYCLE#'].tolist()

deg_j_600mV = []
deg_j_400mV = []
deg_asr_600mV = []
deg_asr_400mV = []
deg_asr_0mV = []
deg_timer = []

for i in range(0, len(ast_markers)):

    df_ast = df_tb_comp.iloc[ast_markers[i]:iv_markers[i+1]]

    exclusions = ['anfahren_10A', 'anfahren_20A', 'ocv', 'anfahren_I_High', 'anfahren_I_Low', 'halten_I_Low',
                 'halten_I_High']

    df_ast = df_ast[~df_ast['Kommentar'].isin(exclusions)]

    df_ast = df_ast.reset_index(drop=True)

    ast_start = df_ast['T relativ [min]'][0]

    df_ast['t elapsed [s]'] = (df_ast['T relativ [min]'] - ast_start) / 60

    name = 'AST#' + str(i+1) + '_' + df_tb_comp['Datum / Uhrzeit'][ast_markers[i]][:8]

    deg_j_600mV.append(df_ast[df_ast['Kommentar'] == 'operation@0.6V']['mean current density [A/cm2]'].mean())
    deg_j_400mV.append(df_ast[df_ast['Kommentar'] == 'operation@0.4V']['mean current density [A/cm2]'].mean())
    deg_asr_600mV.append(df_ast[df_ast['Kommentar'] == 'operation@0.6V']['ASR [mOhm*cm2]'].mean())
    deg_asr_400mV.append(df_ast[df_ast['Kommentar'] == 'operation@0.4V']['ASR [mOhm*cm2]'].mean())
    deg_asr_0mV.append(df_ast[df_ast['Kommentar'] == 'OCV']['ASR [mOhm*cm2]'].mean())
    deg_timer.append(i * 25)

    df_ast = df_ast[['timer', 't elapsed [s]', 'AI.U.E.Co.Tb.1 [V]', 'AI.T.Air.ST.UUT.out [°C]', 'current density [A/cm2]', 'HFR [mOhm]',
                     'mean current density [A/cm2]']]

    df_ast.to_csv(r'data\dashdata' + '/' + name)


df_deg = pd.DataFrame(data={'deg_j_@400mV': deg_j_400mV, 'deg_j_@600mV': deg_j_600mV,
                            'deg_asr_@400mV': deg_asr_400mV, 'deg_asr_@600mV': deg_asr_600mV,
                            'deg_asr_@0mV': deg_asr_0mV, 'timer': deg_timer})




df_deg.to_csv(r'data\dashdata' + '/' + 'DEG')



# SAVE DATAFRAMES - EIS
for i in range(0, len(eis_dfs)):
    name = 'EIS#' + str(i) + '_' + eis_files[i]
    eis_dfs[i].to_csv(r'data\dashdata' + '/' + name)



# SAVE DATAFRAMES - CV
for i in range(0, len(cv1_dfs)):
    name = 'CV#' + str(i) + '_' + cv1_files[i]
    cv1_dfs[i].to_csv(r'data\dashdata' + '/' + name)


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

