# %%
import pandas as pd

# %%
cbsa_team_codes = [['COL', 'Denver-Aurora-Lakewood, CO', '19740'], \
                ['MIN', 'Minneapolis-St. Paul-Bloomington, MN-WI', '33460'], \
                ['MIL', 'Milwaukee-Waukesha-West Allis, WI', '33340'], \
                ['CHC', 'Chicago-Naperville-Elgin, IL-IN-WI', '16980'], \
                ['CHW', 'Chicago-Naperville-Elgin, IL-IN-WI', '16980'], \
                ['KCR', 'Kansas City, MO-KS', '28140'], \
                ['STL', 'St. Louis, MO-IL', '41180'], \
                ['DET', 'Detroit-Warren-Dearborn, MI', '19820'], \
                ['CLE', 'Cleveland-Elyria-Mentor, OH', '17460'], \
                ['CIN', 'Cincinnati, OH-KY-IN', '17140'], \
                ['PIT', 'Pittsburgh, PA', '38300'], \
                ['PHI', 'Philadelphia-Camden-Wilmington, PA-NJ-DE', '37980']]

# %%
df = pd.DataFrame(cbsa_team_codes, columns=['team', 'msa', 'cbsa_code'])

# %%
zip_crosswalk = pd.read_csv('../crosswalk/zip_cbsa.csv', dtype={'ZIP':'str', 'CBSA':'str'})

# %%
zip_crosswalk = zip_crosswalk.rename(columns={'ZIP':'zip', 'CBSA':'cbsa_code', 'USPS_ZIP_PREF_CITY':'city', 'USPS_ZIP_PREF_STATE':'state'})

# %%
zip_crosswalk = zip_crosswalk.drop(columns=['RES_RATIO', 'BUS_RATIO', 'OTH_RATIO', 'TOT_RATIO'])

# %%
zip_crosswalk_teams = zip_crosswalk.merge(df, how='left', on='cbsa_code')

# %%
state_survey_clean = pd.read_csv('../fin_table/state_survey_clean.csv', dtype={'zip':'str'})

# %%
state_survey_merged = state_survey_clean.merge(zip_crosswalk_teams, how='left', on='zip')

# %%
#state_survey_merged.to_csv('../fin_table/state_survey_merged.csv')

# %%
teams = df['team']

# %%
def team_survey_data(team_list):
    for team in team_list:
        team_df = state_survey_merged.loc[state_survey_merged['team'] == team]
        team_df.to_csv('../team_data/' + team + '_data.csv')

# %%
team_survey_data(teams)


