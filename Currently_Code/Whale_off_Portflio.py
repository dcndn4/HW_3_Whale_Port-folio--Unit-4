# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:51:55 2021

@author: CS_Knit_tinK_SC
"""

# Initial imports
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path

%matplotlib inline


#%%

#file_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/loans.csv"
#csv_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/goog_google_finance.csv"
csv_path_w = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/Whale/whale_returns.csv"
whale_returns = pd.read_csv(
    csv_path_w, parse_dates=True, index_col="Date", infer_datetime_format=True
)

# whale df is 1060/4
print(whale_returns.head())
#%%

# Count nulls
print(whale_returns.isnull().mean() * 100)

#%%

whale_returns=whale_returns.dropna()


#%%

#file_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/loans.csv"
#csv_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/goog_google_finance.csv"
csv_path_a = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/Whale/algo_returns.csv"
algo_returns = pd.read_csv(
    csv_path_a, parse_dates=True, index_col="Date", infer_datetime_format=True
)

# algo df is 1241/2
print(algo_returns.head())

#%%

# Count nulls
print(algo_returns.isnull().mean() * 100)

#%%

algo_returns=algo_returns.dropna()

#%%

#file_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/loans.csv"
#csv_path = Path="C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/goog_google_finance.csv"
csv_path_s = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/Whale/sp500_history.csv"
#sp500_history = pd.read_csv(
#csv_path_s, parse_dates=True, index_col="Date", infer_datetime_format=True
#)
sp500_history = pd.read_csv(csv_path_s)

# sp500 is 1649/2
print(sp500_history.head())

#%%

# Check Data Types
print(sp500_history.dtypes)

#%%

#Set index as date field

#sp500_history.set_index(sp500_history['Date'], inplace=True)
#print(sp500_history.head())
sp500_history.set_index(pd.to_datetime(sp500_history['Date'], infer_datetime_format=True), inplace=True)
sp500_history.sort_index(inplace=True)
print(sp500_history.head())


#%%

# Fix Data Types


sp500_history['Close'] = sp500_history['Close'].str.replace('$','')
sp500_history['Close']=sp500_history['Close'].astype('float')


#%%
# Drop the extra date column
sp500_history.drop(columns=['Date'], inplace=True)
print(sp500_history.head())
print(sp500_history.dtypes)

#%%

sp500_history=sp500_history.dropna()

#%%

sp500_returns = sp500_history.pct_change()

#%%

sp500_returns.columns = ["SP500"] 

#%%

all_returns = pd.concat([algo_returns, whale_returns, sp500_returns], axis='columns', join = 'inner')

#%%

# Plot daily returns of all portfolios
algo_returns.plot()
whale_returns.plot()
sp500_returns.plot()

#%%

cumulative_algo_returns = (1 + algo_returns).cumprod() - 1
cumulative_whale_returns = (1 + whale_returns).cumprod() - 1
cumulative_sp500_returns = (1 + sp500_returns).cumprod() - 1

#%%

cumulative_algo_returns.plot()
cumulative_whale_returns.plot()
cumulative_sp500_returns.plot()

#%%

all_returns.plot.box()

#%%
daily_std = all_returns.std()
print(f' Daily Standard Returns are: \n{daily_std}')

#%%

# Calculate  the daily standard deviation of S&P 500

print(f' The daily Standard Returns are: \n{daily_std}')

# Calculate  the daily standard deviation of S&P 500

daily_std = daily_std.sort_values(ascending=False)



# Determine which portfolios are riskier than the S&P 500
# do for loop, identify items in riskier file??
#%%

# Calculate the annualized standard deviation (252 trading days)
annualized_std = daily_std * np.sqrt(252)
annualized_std = annualized_std.sort_values(ascending=False)
print(annualized_std)

#%%

#Rolling Statistics

#Risk changes over time. Analyze the rolling statistics for Risk and Beta.

#Calculate and plot the rolling standard deviation for all portfolios
# using a 21-day window
#Calculate the correlation between each stock to determine which 
#portfolios may mimic the S&P 500
#Choose one portfolio, then calculate and plot the 60-day rolling beta
# between it and the S&P 500



#%%

# Calculate and plot rolling std for all portfolios with 21-day window

# Calculate the rolling standard deviation for all portfolios using a 21-day window


#all_returns.rolling(window=21).std()   

# Plot the rolling standard deviation
#all_returns.rolling(window=21).std().plot

algo_returns.rolling(window=21).std().plot()
whale_returns.rolling(window=21).std().plot()
sp500_returns.rolling(window=21).std().plot()
#%%

# Calculate the correlation
correlation = all_returns.corr()
# Display the correlation matrix
print(correlation)
correlation.plot()

#%%

# Calculate covariance of a single portfolio
covariance = all_returns['Algo 1'].cov(all_returns['SP500'])

# Calculate variance of S&P 500
variance = all_returns['SP500'].var()

# Computing beta
Algo1_beta = covariance/variance

#%%

# Plot beta trend
rolling_Algo1_covariance = all_returns['Algo 1'].rolling(window=30).cov(all_returns['SP500'])
rolling_variance = all_returns['SP500'].rolling(window=30).var()
rolling_Algo1_beta = rolling_Algo1_covariance / rolling_variance
ax = rolling_Algo1_beta.plot(figsize=(20, 10), title='Rolling 30-Day Beta of Algo 1')

#%%