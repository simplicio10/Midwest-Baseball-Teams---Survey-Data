# %%
import pandas as pd

# %%
feb_24 = pd.read_csv('../survey_data/feb_2024_data.csv')
oct_23 = pd.read_csv('../survey_data/oct_2023_data.csv')

# %%
print(oct_23.columns)
print(feb_24.columns)

# %%
oct_23.drop(columns=['Midwesterner', 'Born', 'Ideology', 'Partyregaff', 'Age', 'race', 'otehistory', 'education', 'gender', 'weight'], inplace=True)


# %%
oct_23 = oct_23.rename(columns={'State': 'state', 'Midwest': 'midwest'})

# %%
feb_24.drop(columns=['What is your party affiliation/registration?', 'What is your age range?', 'For statistical purposes only, can you please tell me your ethnicity?', 'What is the highest level of education you have attained?', 'Can you please tell me your gender?', 'ZIP3', 'weights'], inplace=True)

# %%
feb_24 = feb_24.rename(columns={'Do you live in the Midwest or the South?': 'midwest_1', 'Do you live in the Midwest, the Great Plains, or the West?': 'midwest_2', 'Do you live in the Midwest, Appalachia, or the South?': 'midwest_3', 'ZIP':'zip', 'STATE':'state'})

# %%
feb_24.head()

# %%
mw_feb_ones = feb_24.loc[feb_24['midwest_1'] != '#NULL!']
mw_feb_twos = feb_24.loc[feb_24['midwest_2'] != '#NULL!']
mw_feb_threes = feb_24.loc[feb_24['midwest_3'] != '#NULL!']

# %%
mw_feb_ones.drop(columns=['midwest_2', 'midwest_3'], inplace=True)
mw_feb_twos.drop(columns=['midwest_1', 'midwest_3'], inplace=True)
mw_feb_threes.drop(columns=['midwest_1', 'midwest_2'], inplace=True)

# %%
mw_feb_ones = mw_feb_ones.rename(columns={'midwest_1':'midwest'})
mw_feb_twos = mw_feb_twos.rename(columns={'midwest_2':'midwest'})
mw_feb_threes = mw_feb_threes.rename(columns={'midwest_3':'midwest'})

# %%
to_combine = [mw_feb_ones, mw_feb_twos, mw_feb_threes]
mw_combined = pd.concat(to_combine)

# %%
mw_combined['midwest'].replace('3', '2', inplace=True)

# %%
states_feb = ['1', '2', '3', '4']
states_oct = ['7', '21', '41', '49']
mw_combined['state'].replace(states_feb, states_oct, inplace=True)

# %%
tables = [oct_23, mw_combined]
final = pd.concat(tables)

# %%
final.head()

# %%
final.to_csv('../fin_table/state_survey_clean.csv')

# %%
ohio = mw_combined.loc[mw_combined['state'] == 3]

# %%
mw_feb_ones.info()
mw_feb_twos.info()
mw_feb_threes.info()

# %%
mw_combined.info()

# %%



