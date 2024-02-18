#This code uses the cleaned and merged survey data to create a table that summarizes the survey results for each team.

import pandas as pd

survey = pd.read_csv('fin_table/state_survey_merged.csv', dtype={'cbsa_code':'str'})
survey = survey.drop(columns=['Unnamed: 0.1', 'Unnamed: 0', 'state_x'])
survey = survey.loc[survey['team'].notnull() == True]

yes_mw = survey.loc[survey['midwest'] == 1]
yes_mw_team = yes_mw.groupby('team').count()
yes_count = yes_mw_team['midwest']

no_mw = survey.loc[survey['midwest'] == 2]
no_mw_team = no_mw.groupby('team').count()
no_count = no_mw_team['midwest']

final_results = pd.concat([yes_count, no_count], axis=1, keys=['yes_mw', 'no_mw'])
final_results['total_responses'] = final_results.apply(lambda row: row['yes_mw'] + row['no_mw'], axis=1)
final_results['pct_midwest'] = final_results.apply(lambda row: row['yes_mw'] / (row['total_responses']), axis=1)

final_results.to_csv('team_data/results_by_team.csv')


