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