import pandas as pd

# reads csv file
df = pd.read_csv('covid-data.csv')

df['date'] = pd.to_datetime(df['date'])

# shows the first 50 columns
pd.set_option('display.max_columns', 50)

# during 31/10/2020 - 06/11/2020 it shows new cases
df_greece_first_quarantine = df[
    (df['location'] == 'Greece') & ((df['date'] >= '2020-10-31') & (df['date'] <= '2020-11-06'))]  # A3
df_greece_first_quarantine['new_cases']

# during 22/03/2020 - 16/03/2020 it shows new cases
df_greece_second_quarantine = df[
    (df['location'] == 'Greece') & ((df['date'] >= '2020-03-16') & (df['date'] <= '2020-03-22'))]  # A3
df_greece_second_quarantine['new_cases']


#A1
date_march = df[(df['date'] == '2020-03-23') & (df['location'] != 'World')]['total_cases'].max()
df.loc[df['total_cases'] == date_march]

#A2
dates = df[(df['date'] >= '2020-03-23') & (df['date'] <= '2020-03-29')]['new_cases'].max()
df.loc[df['total_cases'] == dates]