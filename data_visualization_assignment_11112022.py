#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:19:41 2022

@author: Chimaroke Amaike
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_health_data = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')


#Extracting Month and Year from the Date_reported column
df_health_data['Year'] = pd.DatetimeIndex(df_health_data['Date_reported']).year
df_health_data['Month'] = pd.DatetimeIndex(df_health_data['Date_reported']).month


#function to extract new data frame from specific columns
#this accepts only 2 columns at the moment

def create_df(column_one, column_one_value, column_two, column_two_value):
    ''' Takes 4 arguments. 2 arguments are the column name, while the other 2 are values used to retrieve the data from the data frame'''
    df = df_health_data[(df_health_data[column_one] == column_one_value) & (df_health_data[column_two] == column_two_value)]
    df_cases = df.groupby(["Month"])[["New_cases","New_deaths"]].sum()
    if column_two_value == 2022:
        #since 2022 does not have data for december, an if statement is used to manage data retreived to so that it does not throw an error
        df_cases['New Month'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']
    else:
        df_cases['New Month'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return df_cases


#This is the first figure of  a line chart showing the daath rate in 3 countries in 2020

plt.figure(figsize=(10, 10))

plt.plot(create_df('Country_code', 'FR', 'Year', 2020)['New Month'], create_df('Country_code', 'FR', 'Year', 2020)['New_deaths'], label = 'FR Death Rate')
plt.plot(create_df('Country_code', 'AU', 'Year', 2020)['New Month'], create_df('Country_code', 'AU', 'Year', 2020)['New_deaths'], label = 'AU Death Rate')
plt.plot(create_df('Country_code', 'CA', 'Year', 2020)['New Month'], create_df('Country_code', 'CA', 'Year', 2020)['New_deaths'], label = 'CA Death Rate')
plt.plot(create_df('Country_code', 'GB', 'Year', 2020)['New Month'], create_df('Country_code', 'GB', 'Year', 2020)['New_deaths'], label = 'GB Death Rate')
plt.xticks(rotation='vertical')

plt.xlabel("Months")
plt.ylabel("Death Rate")
plt.title('Date Rate comparison across 4 countries in 2020')
plt.legend()

plt.savefig('date_rate.png')

plt.show()





#comparing New Cases and Deaths per region

#generate date for 4 regions:

def sum_of_columns(year,column_to_be_sumed,region):
    ''' This accepts 3 positional argument. The result is the sum of the column selected per region as specified'''
    
    regional_sum = create_df('WHO_region', region, 'Year', year)[column_to_be_sumed].sum()
    return regional_sum



who_regions = [sum_of_columns(2022, 'New_deaths', 'EURO'), sum_of_columns(2022, 'New_deaths', 'AFRO'), sum_of_columns(2022, 'New_deaths', 'WPRO'), sum_of_columns(2022, 'New_deaths', 'AMRO')]
who_regions_label = ['EURO', 'AFRO', 'WPRO', 'AMRO']
explode = (0.1, 0, 0, 0)  

def draw_pie_chart(sumed_regions, explode, who_regions_label):
    ''' accepts 3 positional argument used to render a pie chart. This can be reused at anytime.'''
    
    plt.figure(figsize=(10, 10))
    plt.pie(sumed_regions, explode=explode, labels=who_regions_label, autopct='%1.3f%%', shadow=True, startangle=90)
    plt.title('New Deaths per Region')
    plt.savefig('date_rate_per_region_2022.png')
    plt.show()


draw_pie_chart(who_regions, explode, who_regions_label)





months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
width = 0.35

def random_number(num):
    ''' This function is used to generate numbers serially from 0 to the specified number - num'''
    ind = np.arange(len(num))
    return ind

plt.figure(figsize=(10, 10))

euro_2020 = create_df('WHO_region', 'EURO', 'Year', 2020)['New_cases'].tolist()
bar_2020 = plt.bar(random_number(months), euro_2020, width, color='r')
  
euro_2021 = create_df('WHO_region', 'EURO', 'Year', 2021)['New_cases'].tolist()
bar_2021 = plt.bar(random_number(months)+width, euro_2021, width, color='g')
  
plt.xlabel("Number of Covid-19 Cases")
plt.ylabel('New Cases')
plt.title("Covid-19 Cases in Europe Region 2020 vs 2021")
  
plt.xticks(random_number(months)+width,months,rotation='vertical')
plt.legend( (bar_2020, bar_2021), ('2020', '2021'))
plt.savefig('new_cases_2020_2021png')
plt.show()