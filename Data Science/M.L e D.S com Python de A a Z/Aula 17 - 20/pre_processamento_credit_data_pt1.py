# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:37:21 2020

@author: Gabriel
"""

import pandas as pd
base = pd.read_csv('credit-data.csv')
base.describe()