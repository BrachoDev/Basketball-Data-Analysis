# THIS CODE IS FOR REFERENCE ONLY. THIS WILL NOT RUN
# THE CODE IS SEPARATED IN STEPS FROM 1 TO 6:

# Step 1: Data Preparation

import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

# dataframe for this project
nba_wins_df = pd.read_csv('nba_wins_data.csv')

display(HTML(nba_wins_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(nba_wins_df))

# Step 2: Scatterplot and Correlation for the Total Number of Wins and Average Relative Skill

import scipy.stats as st

# ---- TODO: make your edits here ----
plt.plot(nba_wins_df['avg_elo_n'], nba_wins_df['total_wins'], 'o')

plt.title('Total Number of Wins by Average Relative Skill', fontsize=20)
plt.xlabel('Average Relative Skill')
plt.ylabel('Total Number of Wins')
plt.show()


# ---- TODO: make your edits here ----
correlation_coefficient, p_value = st.pearsonr(nba_wins_df['avg_elo_n'], nba_wins_df['total_wins'])

print("Correlation between Average Relative Skill and the Total Number of Wins ")
print("Pearson Correlation Coefficient =",  round(correlation_coefficient,4))
print("P-value =", round(p_value,4))

# Step 3: Simple Linear Regression: Predicting the Total Number of Wins using Average Relative Skill

import statsmodels.formula.api as smf

# Simple Linear Regression
# ---- TODO: make your edits here ---
model1 = smf.ols('total_wins ~ avg_elo_n', nba_wins_df).fit()
print(model1.summary())

# Step 4: Scatterplot and Correlation for the Total Number of Wins and Average Points Scored

import scipy.stats as st

# ---- TODO: make your edits here ----
plt.plot(nba_wins_df['avg_pts'], nba_wins_df['total_wins'], 'o')

plt.title('Total Number of Wins by Average Points Scored', fontsize=20)
plt.xlabel('Average Points Scored')
plt.ylabel('Total Number of Wins')
plt.show()


# ---- TODO: make your edits here ----
correlation_coefficient, p_value = st.pearsonr(nba_wins_df['avg_pts'], nba_wins_df['total_wins'])

print("Correlation between Average Points Scored and the Total Number of Wins ")
print("Pearson Correlation Coefficient =",  round(correlation_coefficient,4))
print("P-value =", round(p_value,4))

# Step 5: Multiple Regression: Predicting the Total Number of Wins using Average Points Scored and Average Relative Skill

import statsmodels.formula.api as smf

# Multiple Regression
# ---- TODO: make your edits here ---
model2 = smf.ols('total_wins ~ avg_elo_n + avg_pts', nba_wins_df).fit()
print(model2.summary())

# Step 6: Multiple Regression: Predicting the Total Number of Wins using Average Points Scored, Average Relative Skill, Average Points Differential and Average Relative Skill Differential

# Write your code in this code block section
import statsmodels.formula.api as smf

# Multiple Regression
# ---- TODO: make your edits here ---
model3 = smf.ols('total_wins ~ avg_elo_n + avg_pts + avg_pts_differential + avg_elo_differential', nba_wins_df).fit()
print(model3.summary())