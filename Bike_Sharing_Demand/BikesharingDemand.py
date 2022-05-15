"""
@ 2022-05-15
BikeSaringDemand class화
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

import os

class bikesharingdemand:
    def __init__(self, kaggle_user_name, kaggle_key):
        self.kaggle_user_name = ''
        self.kaggle_key = ''
    
    def import_data(self):
        # os.environ을 이용하여 Kaggle API Username, Key 세팅하기
        os.environ['KAGGLE_USERNAME'] = kaggle_user_name
        os.environ['KAGGLE_KEY'] = kaggle_key

        # Linux 명령어로 Kaggle API를 이용하여 데이터셋 다운로드하기 (!kaggle ~)
        # Linux 명령어로 압축 해제하기
        !rm *.*
        !kaggle competitions download -c bike-sharing-demand
        !unzip '*.zip'

        train = pd.read_csv('train.csv', parse_dates = ['datetime'])
        test  = pd.read_csv('test.csv' , parse_dates = ['datetime'])

    @staticmethod
    def day_of_week(day):
        if   day == 0:
            return 'Mon'
        elif day == 1:
            return 'Tue'
        elif day == 2:
            return 'Wed'
        elif day == 3:
            return 'Thur'
        elif day == 4:
            return 'Fri'
        elif day == 5:
            return 'Sat'
        elif day == 6:
            return 'Sun'
        else:
            return 'err'

    def preprocessing(self):
        # Train
        # 시간변수
        train['year']  = train['datetime'].dt.year
        train['month'] = train['datetime'].dt.month
        train['day']   = train['datetime'].dt.day
        train['hour']  = train['datetime'].dt.hour
        train['min']   = train['datetime'].dt.minute
        train['sec']   = train['datetime'].dt.second
        train['dow']   = train['datetime'].dt.dayofweek

        train['dow_humanized'] = train['dow'].apply(day_of_week)


        # Test
        test['year']  = test['datetime'].dt.year
        test['month'] = test['datetime'].dt.month
        test['day']   = test['datetime'].dt.day
        test['hour']  = test['datetime'].dt.hour
        test['min']   = test['datetime'].dt.minute
        test['sec']   = test['datetime'].dt.second
        test['dow']   = test['datetime'].dt.dayofweek

        test['dow_humanized'] = test['dow'].apply(day_of_week)

    def run(self):
        return result