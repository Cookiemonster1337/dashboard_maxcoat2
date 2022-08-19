import pandas as pd
import os
import plotly.graph_objects as go

datafolder = r'data\dashdata'

# ----------------------------------------------------------------------------------------------------------------------
# GRAPHDATA - TESTBENCH
# ----------------------------------------------------------------------------------------------------------------------
df_tb = pd.read_csv(datafolder + '/df_testrig.csv')

tb_voltage = df_tb['AI.U.E.Co.Tb.1 [V]']
tb_temp = df_tb['AI.T.Air.ST.UUT.out [°C]']
tb_hfr = df_tb['HFR [mOhm]'].apply(lambda x: x if x != -99 and x < 100 else None)
tb_j = df_tb['current density [A/cm2]']
duration = df_tb['duration [s]'] / 3600

trace_1 = go.Scatter(
        x=duration,
        y=tb_voltage,
        name='voltage [V]',
        yaxis='y2',
        visible='legendonly'
        )

trace_2 = go.Scatter(
        x=duration,
        y=tb_temp,
        name='temperature [°C]',
        yaxis='y2',
        visible='legendonly'
        )

trace_3 = go.Scatter(
        x=duration,
        y=tb_hfr*25,
        name='ASR [mOhm*cm2]',
        yaxis='y2',
        visible='legendonly'
        )

trace_4 = go.Scatter(
        x=duration,
        y=tb_j,
        name='current density [A/cm2]',
        yaxis='y1'
        )

tb_data = [trace_1, trace_2, trace_3, trace_4]

# ----------------------------------------------------------------------------------------------------------------------
# TABLEDATA - AST
# ----------------------------------------------------------------------------------------------------------------------
df_param_ast = pd.read_csv(datafolder + '/parameters_ast.csv', encoding='cp1252', delimiter=';')
df_param_pol = pd.read_csv(datafolder + '/parameters_pol.csv', encoding='cp1252', delimiter=';')


# ----------------------------------------------------------------------------------------------------------------------
# GRAPHDATA - AST
# ----------------------------------------------------------------------------------------------------------------------
dfs_ast = [pd.read_csv(datafolder + '/' + f) for f in os.listdir(datafolder) if 'AST' in f]
ast_names = [str(f) for f in os.listdir(datafolder) if 'AST' in f]

ast_data = []
ast_durations = []

for i in range(0, len(dfs_ast)):
        df_ast = dfs_ast[i]

        current_density = df_ast['current density [A/cm2]']
        duration = df_ast['t elapsed [s]']

        ast_name = ast_names[i][:5]

        ast_data.append(go.Scatter(x=duration, y=current_density, name=ast_name))

        ast_durations.append(abs(int((pd.to_datetime(df_ast['timer'][df_ast.index[0]], format='%Y-%m-%d %H:%M:%S') -
                                      pd.to_datetime(df_ast['timer'][df_ast.index[-1]],
                                                     format='%Y-%m-%d %H:%M:%S')).total_seconds()
                                     / 3600)))
# ----------------------------------------------------------------------------------------------------------------------
# GRAPHDATA - DEG
# ----------------------------------------------------------------------------------------------------------------------
df_deg = pd.read_csv(datafolder + '/' + 'DEG', index_col=0)

timer = df_deg['timer']
trace_1 = go.Scatter(
        x=timer,
        y=df_deg['deg_j_@400mV'],
        name='potential @400mV',
        yaxis='y1'
        )


trace_2 = go.Scatter(
        x=timer,
        y=df_deg['deg_asr_@400mV'],
        name='ASR @400mV',
        yaxis='y2',
        visible='legendonly'
        )

trace_3 = go.Scatter(
        x=timer,
        y=df_deg['deg_j_@600mV'],
        name='potential @600mV',
        yaxis='y1',
        )


trace_4 = go.Scatter(
        x=timer,
        y=df_deg['deg_asr_@600mV'],
        name='ASR @600mV',
        yaxis='y2',
        visible='legendonly'
        )

trace_5 = go.Scatter(
        x=timer,
        y=df_deg['deg_asr_@0mV'],
        name='ASR @0mV',
        yaxis='y2',
        visible='legendonly'
        )

deg_data = [trace_1, trace_2, trace_3, trace_4, trace_5]

# ----------------------------------------------------------------------------------------------------------------------
# GRAPHDATA - IV
# ----------------------------------------------------------------------------------------------------------------------
dfs_iv = [pd.read_csv(datafolder + '/' + f) for f in os.listdir(datafolder) if 'POL' in f]
iv_names = [str(f) for f in os.listdir(datafolder) if 'POL' in f]

iv_data = []
iv_durations = []

for i in range(0, len(dfs_iv)):
        df_iv = dfs_iv[i]
        current_densities = pd.unique(df_iv['current density [A/cm2]'])

        mean_voltages = []

        for j in current_densities:
                mean_voltages.append(
                        df_iv[df_iv['current density [A/cm2]'] == j]['AI.U.E.Co.Tb.1 [V]'].mean())

        iv_name = iv_names[i][:5]

        iv_data.append(go.Scatter(x=current_densities, y=mean_voltages, name=iv_name))

        iv_durations.append(abs(int((pd.to_datetime(df_iv['timer'][df_iv.index[0]], format='%Y-%m-%d %H:%M:%S') -
                                     pd.to_datetime(df_iv['timer'][df_iv.index[-1]],
                                                    format='%Y-%m-%d %H:%M:%S')).total_seconds()
                                    / 3600) + 1))
# ----------------------------------------------------------------------------------------------------------------------
# GRAPHDATA - EIS
# ----------------------------------------------------------------------------------------------------------------------
dfs_eis = [pd.read_csv(datafolder + '/' + f) for f in os.listdir(datafolder) if 'EIS' in f]
eis_names = [str(f) for f in os.listdir(datafolder) if 'EIS' in f]

eis_data = []

for i in range(0, len(dfs_eis)):
        df_eis = dfs_eis[i]

        impedance_real = df_eis['Z_real [Ohm]'] * 25
        impedance_imag = df_eis['Z_imag [Ohm]'] * -25

        eis_name = eis_names[i][:5]

        eis_data.append(go.Scatter(x=impedance_real, y=impedance_imag, name=eis_name))

# ----------------------------------------------------------------------------------------------------------------------
# GRAPHDATA - CV
# ----------------------------------------------------------------------------------------------------------------------
dfs_cv1 = [pd.read_csv(datafolder + '/' + f) for f in os.listdir(datafolder) if 'CV1.1' in f]
cv1_names = [str(f) for f in os.listdir(datafolder) if 'CV1.1' in f]

cv1_data = []

for i in range(0, len(dfs_cv1)):
        df_cv1 = dfs_cv1[i]

        voltage = df_cv1['voltage [V]'][38571:] * -1
        current = df_cv1['current [A]'][38571:] * -1

        cv1_name = cv1_names[i][:4]

        if i == 5:
                cv1_data.append(go.Scatter(x=voltage, y=current, name=cv1_name, visible='legendonly'))
        else:
                cv1_data.append(go.Scatter(x=voltage, y=current, name=cv1_name))

# ----------------------------------------------------------------------------------------------------------------------
# SUMMARY
# ----------------------------------------------------------------------------------------------------------------------
summary = {}
time_op = df_tb['duration [s]'].max() / 3600


summary['time of operation [h]'] = int(time_op)
summary['duration of ASTs [h]'] = sum(ast_durations)
summary['duration of CHARs [h]'] = sum(iv_durations)
summary['duration of Conditioning [h]'] = 36

sum_data_tr = go.Pie(labels=['COND', 'AST', 'CHAR'],
                         values=[summary['duration of Conditioning [h]'], summary['duration of ASTs [h]'],
                                 summary['duration of CHARs [h]']], hole=.5)