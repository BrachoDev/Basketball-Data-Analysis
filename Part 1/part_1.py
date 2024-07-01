# THIS CODE IS FOR REFERENCE ONLY. THIS WILL NOT RUN
# THE CODE IS SEPARATED IN STEPS FROM 1 TO 9:

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
# The assigned team is the Chicago Bulls from 1996-1998.
assigned_years_league_df = nba_orig_df[(nba_orig_df['year_id'].between(1996, 1998))]
assigned_team_df = assigned_years_league_df[(assigned_years_league_df['fran_id']=='Bulls')]
assigned_team_df = assigned_team_df.reset_index(drop=True)

display(HTML(assigned_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the data set =", len(assigned_team_df))

# Step 2: Picking a Team (Warriors)

# Range of years: 2013-2015 (Note: The line below selects ALL teams within the three-year period 2013-2015. This is not your team's dataframe.
your_years_leagues_df = nba_orig_df[(nba_orig_df['year_id'].between(2013, 2015))]

# The dataframe for your team is called your_team_df.
# ---- TODO: make your edits here ----
your_team_df = your_years_leagues_df[(your_years_leagues_df['fran_id']=='Warriors')]
your_team_df = your_team_df.reset_index(drop=True)

display(HTML(your_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the data set =", len(your_team_df))

# Step 3: Data Visualization: Points Scored by the Team

import seaborn as sns

# Histogram
fig, ax = plt.subplots()
plt.hist(your_team_df['pts'], bins=20)
plt.title('Histogram of points scored by Your Team in 2013 to 2015', fontsize=18)
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')
plt.show()
print("")

# Scatterplot
plt.title('Scatterplot of points scored by Your Team in 2013 to 2015', fontsize=18)
sns.regplot(your_team_df['year_id'], your_team_df['pts'], ci=None)
plt.show()

# Step 4: Data Visualization: Points Scored by the Chicago Bulls

import seaborn as sns

# Histogram
fig, ax = plt.subplots()
plt.hist(assigned_team_df['pts'], bins=20)
plt.title('Histogram of points scored by the Bulls in 1996 to 1998', fontsize=18)
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')
plt.show()

# Scatterplot
plt.title('Scatterplot of points scored by the Bulls in 1996 to 1998', fontsize=18)
sns.regplot(assigned_team_df['year_id'], assigned_team_df['pts'], ci=None)
plt.show()

# Step 5: Data Visualization: Comparing the Two Teams

import seaborn as sns

# Side-by-side boxplots
both_teams_df = pd.concat((assigned_team_df, your_team_df))
plt.title('Boxplot to compare points distribution', fontsize=18) 
sns.boxplot(x='fran_id',y='pts',data=both_teams_df)
plt.show()
print("")

# Histograms
fig, ax = plt.subplots()
plt.hist(assigned_team_df['pts'], 20, alpha=0.5, label='Assigned Team')
plt.hist(your_team_df['pts'], 20, alpha=0.5, label='Your Team')
plt.title('Histogram to compare points distribution', fontsize=18) 
plt.xlabel('Points')
plt.legend(loc='upper right')
plt.show()

# Step 6: Descriptive Statistics: Points Scored By Warriors in Home Games

print("Points Scored by Your Team in Home Games (2013 to 2015)")
print("-------------------------------------------------------")

your_team_home_df = your_team_df[your_team_df['game_location']=='H'].copy()

# ---- TODO: make your edits here ----
mean = your_team_home_df['pts'].mean()
median = your_team_home_df['pts'].median()
variance = your_team_home_df['pts'].var()
stdeviation = your_team_home_df['pts'].std()

print('Mean =', round(mean,2))
print('Median =', round(median,2))
print('Variance =', round(variance,2))
print('Standard Deviation =', round(stdeviation,2))

# Step 7 - Descriptive Statistics - Points Scored By Your Time in Away Games

# Write your code in this code block. 
print("Points Scored by Your Team in Away Games (2013 to 2015)")
print("-------------------------------------------------------")

your_team_home_df = your_team_df[your_team_df['game_location']=='A'].copy()

mean = your_team_home_df['pts'].mean()
median = your_team_home_df['pts'].median()
variance = your_team_home_df['pts'].var()
stdeviation = your_team_home_df['pts'].std()

print('Mean =', round(mean,2))
print('Median =', round(median,2))
print('Variance =', round(variance,2))
print('Standard Deviation =', round(stdeviation,2))

# Step 8: Confidence Intervals for the Average Relative Skill of All Teams in Your Team's Years

print("Confidence Interval for Average Relative Skill in the years 2013 to 2015")
print("------------------------------------------------------------------------------------------------------------")

# Mean relative skill of all teams from the years 2013-2015
mean = your_years_leagues_df['elo_n'].mean()

# Standard deviation of the relative skill of all teams from the years 2013-2015
stdev = your_years_leagues_df['elo_n'].std()

n = len(your_years_leagues_df)

#Confidence interval
# ---- TODO: make your edits here ----
stderr = stdev/(n ** 0.5)
conf_int_95 = st.norm.interval(0.95, mean, stderr)

print("95% confidence interval (unrounded) for Average Relative Skill (ELO) in the years 2013 to 2015 =", conf_int_95)
print("95% confidence interval (rounded) for Average Relative Skill (ELO) in the years 2013 to 2015 = (",  round(conf_int_95[0], 2),",", round(conf_int_95[1], 2),")")


print("\n")
print("Python Method to calculate probability that a team has Average Relative Skill LESS than the Average Relative Skill (ELO) of your team in the years 2013 to 2015")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")

mean_elo_your_team = your_team_df['elo_n'].mean() 

choice1 = st.norm.sf(mean_elo_your_team, mean, stdev) 
choice2 = st.norm.cdf(mean_elo_your_team, mean, stdev)

# Pick the correct answer.
print("Which of the two choices is correct?")
print("Choice 1 =", round(choice1,4))
print("Choice 2 =", round(choice2,4))

# Step 9: Confidence Intervals for the Average Relative Skill of All Teams in the Assigned Team's Years

# Write your code in this code block section
print("Confidence Interval for Average Relative Skill in the years 1996 to 1998")
print("------------------------------------------------------------------------------------------------------------")

# Mean relative skill of all teams from the years 2013-2015
mean = assigned_years_league_df['elo_n'].mean()

# Standard deviation of the relative skill of all teams from the years 2013-2015
stdev = assigned_years_league_df['elo_n'].std()

n = len(assigned_years_league_df)

#Confidence interval
stderr = stdev/(n ** 0.5)
conf_int_95 = st.norm.interval(0.95, mean, stderr)

print("95% confidence interval (unrounded) for Average Relative Skill (ELO) in the years 1996 to 1998 =", conf_int_95)
print("95% confidence interval (rounded) for Average Relative Skill (ELO) in the years 1996 to 1998 = (",  round(conf_int_95[0], 2),",", round(conf_int_95[1], 2),")")