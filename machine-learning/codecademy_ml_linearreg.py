# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:33:54 2020

@author: Celestine
"""

import os
os.chdir('d:/Codecademy/tennis_ace_starting/tennis_ace_starting')
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#loading csv file
tennis_stats = pd.read_csv('tennis_stats.csv')

#exploratory analysis (uncomment to plot)
#plt.scatter(tennis_stats['FirstServePointsWon'], tennis_stats['Winnings'], alpha = 0.4, label = 'FirstServe')
#plt.scatter(tennis_stats['SecondServePointsWon'], tennis_stats['Winnings'], alpha = 0.4, label = 'SecondServe')
#plt.scatter(tennis_stats['BreakPointsOpportunities'], tennis_stats['Winnings'], alpha = 0.4)
#plt.scatter(tennis_stats['BreakPointsConverted'], tennis_stats['Winnings'], alpha = 0.4, label = 'Converted')
#plt.scatter(tennis_stats['BreakPointsSaved'], tennis_stats['Winnings'], alpha = 0.4, label = 'Saved')
#plt.scatter(tennis_stats['Aces'], tennis_stats['Winnings'], alpha = 0.4, label = 'Aces')
#plt.scatter(tennis_stats['ServiceGamesWon'], tennis_stats['Winnings'], alpha = 0.4)
#plt.scatter(tennis_stats['ReturnGamesWon'], tennis_stats['Winnings'], alpha = 0.4)
plt.legend()
plt.show()
plt.clf()
# BreakPointsOpportunities have a strong connection with Winnings

#linear regression (BreakPointsOpportunities best to model winnings)
X = tennis_stats[['BreakPointsOpportunities']]
winnings = tennis_stats[['Winnings']]

x_train, x_test, y_train, y_test = train_test_split(X, winnings, train_size = 0.8, test_size = 0.2)

lreg = LinearRegression()
lreg.fit(x_train, y_train)
winnings_predict = lreg.predict(x_test)
model_score = lreg.score(x_test, y_test)

plt.scatter(x_train, y_train, color = 'blue')
plt.plot(x_test, winnings_predict, color = 'orange')
plt.show()
plt.clf()

print(model_score)

#multiple linear regression
tennis_stats['rgw_num'] = tennis_stats['ReturnGamesWon'] * tennis_stats['ReturnGamesPlayed']
tennis_stats['sgw_num'] = tennis_stats['ServiceGamesWon'] * tennis_stats['ServiceGamesPlayed']

df = pd.DataFrame(tennis_stats)
mult_X = df[['Aces', 'BreakPointsFaced', 'BreakPointsOpportunities', 'DoubleFaults', 'rgw_num', 'sgw_num']]
winnings = df[['Winnings']]

x_train, x_test, y_train, y_test = train_test_split(mult_X, winnings, train_size = 0.8, test_size = 0.2)

mlr = LinearRegression()
mlr.fit(x_train, y_train)
winnings_predict = mlr.predict(x_test)
mlr_score = mlr.score(x_test, y_test)

plt.scatter(y_test, winnings_predict, color = 'green')
plt.show()
plt.clf()
print(mlr_score)
#The model produced good results.