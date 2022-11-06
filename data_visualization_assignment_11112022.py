#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:19:41 2022

@author: Chimaroke Amaike
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calendar import month_name

df_health_data = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')


#Extracting Month and Date from the Date_reported column
df_health_data['Year'] = pd.DatetimeIndex(df_health_data['Date_reported']).year
df_health_data['Month'] = pd.DatetimeIndex(df_health_data['Date_reported']).month


def create_df(column_one, column_one_value, column_two, column_two_value):
    df = df_health_data[(df_health_data[column_one] == column_one_value) & (df_health_data[column_two] == column_two_value)]
    df_cases = df.groupby(["Month"])[["New_cases","New_deaths"]].sum()
    if column_two_value == 2022:
        df_cases['New Month'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']
    else:
        df_cases['New Month'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return df_cases

plt.figure()

plt.plot(create_df('Country_code', 'FR', 'Year', 2020)['New Month'] \
         , create_df('Country_code', 'FR', 'Year', 2020)['New_deaths'] \
         , label = 'FR New Deaths')
plt.plot(create_df('Country_code', 'AU', 'Year', 2020)['New Month'] \
         , create_df('Country_code', 'AU', 'Year', 2020)['New_deaths'] \
         , label = 'AU New Deaths')
plt.plot(create_df('Country_code', 'CA', 'Year', 2020)['New Month'] \
         , create_df('Country_code', 'CA', 'Year', 2020)['New_deaths'] \
         , label = 'CA New Deaths')
plt.plot(create_df('Country_code', 'GB', 'Year', 2020)['New Month'] \
         , create_df('Country_code', 'GB', 'Year', 2020)['New_deaths'], label = 'GB New Deaths')
plt.xticks(rotation='vertical')

plt.xlabel("Months in 2020")
plt.ylabel("New Deaths")
plt.legend()

plt.show()