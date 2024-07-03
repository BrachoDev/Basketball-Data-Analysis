# THIS CODE IS FOR REFERENCE ONLY. THIS WILL NOT RUN
# THE CODE IS SEPARATED IN STEPS FROM 1 TO 6:

# Step 1: Data Preparation & the Assigned Team

import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

nba_orig_df = pd.read_csv('nbaallelo.csv')
nba_orig_df = nba_orig_df[(nba_orig_df['lg_id']=='NBA') & (nba_orig_df['is_playoffs']==0)]
columns_to_keep = ['game_id','year_id','fran_id','pts','opp_pts','elo_n','opp_elo_n', 'game_location', 'game_result']
nba_orig_df = nba_orig_df[columns_to_keep]

# The dataframe for the assigned team is called assigned_team_df. 
# The assigned team is the Bulls from 1996-1998.
assigned_years_league_df = nba_orig_df[(nba_orig_df['year_id'].between(1996, 1998))]
assigned_team_df = assigned_years_league_df[(assigned_years_league_df['fran_id']=='Bulls')]
assigned_team_df = assigned_team_df.reset_index(drop=True)

display(HTML(assigned_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(assigned_team_df))

# Step 2: Pick Your Team

# Range of years: 2013-2015 (Note: The line below selects all teams within the three-year period 2013-2015. This is not your team's dataframe.
your_years_leagues_df = nba_orig_df[(nba_orig_df['year_id'].between(2013, 2015))]

# The dataframe for your team is called your_team_df.
# ---- TODO: make your edits here ----
your_team_df = your_years_leagues_df[(your_years_leagues_df['fran_id']== 'Warriors' )]
your_team_df = your_team_df.reset_index(drop=True)

display(HTML(your_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(your_team_df))

# Step 3: Hypothesis Test for the Population Mean (I)

import scipy.stats as st

# Mean relative skill level of your team
mean_elo_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of the Warriors in the years 2013 to 2015 =", round(mean_elo_your_team,2))


# Hypothesis Test
# ---- TODO: make your edits here ----
test_statistic, p_value = st.ttest_1samp(your_team_df['elo_n'],  1340)

print("Hypothesis Test for the Population Mean")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", round(p_value,4)) 

# Step 4: Hypothesis Test for the Population Mean (II)

# Write your code in this code block section
import scipy.stats as st

# Mean relative skill level of your team
mean_elo_your_team = your_team_df['pts'].mean()
print("Mean Points Scored by the Warriors in the years 2013 to 2015 =", round(mean_elo_your_team,2))


# Hypothesis Test
# ---- TODO: make your edits here ----
test_statistic, p_value = st.ttest_1samp(your_team_df['pts'],  106)

print("Hypothesis Test for the Population Mean")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", round(p_value,4)) 

# Step 5: Hypothesis Test for the Population Proportion

from statsmodels.stats.proportion import proportions_ztest

your_team_gt_102_df = your_team_df[(your_team_df['pts'] > 102)]

# Number of games won when your team scores over 102 points
counts = (your_team_gt_102_df['game_result'] == 'W').sum()

# Total number of games when your team scores over 102 points
nobs = len(your_team_gt_102_df['game_result'])

p = counts*1.0/nobs
print("Proportion of games won by the Warriors when scoring more than 102 points in the years 2013 to 2015 =", round(p,4))


# Hypothesis Test
# ---- TODO: make your edits here ----
test_statistic, p_value = proportions_ztest(counts, nobs, 0.90, prop_var=0.90)

print("Hypothesis Test for the Population Proportion")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", round(p_value,4))

# Step 6: Hypothesis Test for the Difference Between Two Population Means¶

import scipy.stats as st

mean_elo_n_project_team = assigned_team_df['elo_n'].mean()
print("Mean Relative Skill of the Bulls in the years 1996 to 1998 =", round(mean_elo_n_project_team,2))

mean_elo_n_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of the Warriors in the years 2013 to 2015  =", round(mean_elo_n_your_team,2))


# Hypothesis Test
# ---- TODO: make your edits here ----
test_statistic, p_value = st.ttest_ind(assigned_team_df['elo_n'], your_team_df['elo_n'])

print("Hypothesis Test for the Difference Between Two Population Means")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", round(p_value,4))