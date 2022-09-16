# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import random
from datetime import datetime

# 경로 데이터 생성
PATH = 'data/slot_data_resource'

dep = pd.read_csv(PATH + '/경로.csv')
dep_list = dep.iloc[:,0].unique().tolist()
route = dep.values.tolist()

# 날짜 데이터 생성(1월 1일 ~ 12월 31일)
def date_range(start, end):
    start = datetime.strptime(start, "%m월 %d일")
    end = datetime.strptime(end, "%m월 %d일")
    dates = [date.strftime("%m월 %d일") for date in pd.date_range(start, periods=(end-start).days+1)]
   
    return dates

# 날짜 슬롯들
date = date_range("1월 1일", "12월 31일")
date_exp = ['오늘','익일','금일','명일','내일','모레','내일 모레', '보름 뒤', '일주일 뒤']
nows = ['지금','당장','빨리','현재','최대한 빨리','가장 빠른','가장 빨리', '빨리빨리']
weeks = ['이번주','다음주','다다음주']
day = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
date_exp_int= ['주 뒤','일 뒤','주일 뒤']

# 단독 사용 가능한 날짜 슬롯
idp_date = pd.Series([date, date_exp, nows, weeks, day], index=['date', 'date_exp', 'now', 'weeks', 'day'])

# 시간 슬롯들
time_exp = ['낮','오전','오후','밤','저녁','아침','새벽']

################# 데이터 생성 함수 #####################
## 경로 생성
def get_route():
    st = random.choice(dep_list)
    match = [i for i in range(len(route)) if route[i][0]==st]
    end = route[random.choice(match)][1]

    return "/DEP;"+st+'/', "/ARR;"+end+'/'

## 날짜 생성
# 1월 1일, 지금, 내일, 보름 뒤, 일주일 뒤, 다음주, 월요일
def get_date(i):
    return '/DATE;'+random.choice(idp_date[i])+'/'

# ex.이번주 월요일, 다음주 월요일
def get_date_with_weeksday():
    return '/DATE;'+random.choice(weeks)+' '+random.choice(day)+'/'

# ex.n주 뒤, n일 뒤
def get_date_exp_int():
    return '/DATE;'+str(np.random.randint(1,20))+random.choice(date_exp_int)+'/'

## 시간 생성
# 출발 시간
#ex. 18시
def get_dtime_hour():
    return '/DEP_TIME;'+str(np.random.randint(0,24))+'시'+'/'

#ex. n시 30분, n시 반
def get_dtime_hourmin():
    return '/DEP_TIME;'+str(np.random.randint(0,24))+'시 ' + random.choice(['반',str(np.random.randint(1,60))+'분'])+'/'

# ex. 낮 n시
def get_dtime_exp_hour():
    return '/DEP_TIME;'+random.choice(time_exp)+' '+str(np.random.randint(1,12))+'시'+'/'

#ex. 낮 n시 n분, 낮 n시 반
def get_dtime_exp_hourmin():
    return '/DEP_TIME;'+random.choice(time_exp)+' '+str(np.random.randint(1,12))+'시 '+random.choice(['반',str(np.random.randint(1,60))+'분'])+'/'

#ex. n시간 뒤
def get_dtime_hour_later():
    return '/DEP_TIME;'+str(np.random.randint(1,12)) + random.choice(['시간 뒤','시간 후'])+'/'

#ex. n분 뒤
def get_dtime_min_later():
    return '/DEP_TIME;'+str(np.random.randint(1,60)) + random.choice(['분 뒤','분 후'])+'/'

#ex. n시간 n분 뒤
def get_dtime_hourmin_later():
    return '/DEP_TIME;'+str(np.random.randint(1,12))+'시간 '+ str(np.random.randint(1,60)) + random.choice(['분 뒤','분 후'])+'/'

# 도착 시간
#ex. 18시
def get_atime_hour():
    return '/DEP_TIME;'+str(np.random.randint(0,24))+'시'+'/'

#ex. n시 30분, n시 반
def get_atime_hourmin():
    return '/ARR_TIME;'+str(np.random.randint(0,24))+'시 ' + random.choice(['반',str(np.random.randint(1,60))+'분'])+'/'

# ex. 낮 n시
def get_atime_exp_hour():
    return '/ARR_TIME;'+random.choice(time_exp)+' '+str(np.random.randint(1,12))+'시'+'/'

#ex. 낮 n시 n분, 낮 n시 반
def get_atime_exp_hourmin():
    return '/ARR_TIME;'+random.choice(time_exp)+' '+str(np.random.randint(1,12))+'시 '+random.choice(['반',str(np.random.randint(1,60))+'분'])+'/'

#ex. n시간 뒤
def get_atime_hour_later():
    return '/ARR_TIME;'+str(np.random.randint(1,12)) + random.choice(['시간 뒤','시간 후'])+'/'

#ex. n분 뒤
def get_atime_min_later():
    return '/ARR_TIME;'+str(np.random.randint(1,60)) + random.choice(['분 뒤','분 후'])+'/'

#ex. n시간 n분 뒤
def get_atime_hourmin_later():
    return '/ARR_TIME;'+str(np.random.randint(1,12))+'시간 '+ str(np.random.randint(1,60)) + random.choice(['분 뒤','분 후'])+'/'

