from gen_data import *
import random

def suhyeon():
    reserve = ["예약", "예매" ,"티켓 발행", "티켓 예약", "티켓 예매","발권"]
    ending = [' 해 줘',' 해 주세요', '하고 싶어','할래','해','하려 하는데 표 있어?', '하고 싶어요','할게요', '할게', ' 부탁합니다', ' 가능해?' , " 가능한가요"]
    
    ########################## generate data - 처음 멘트 #########################
    # case1) 목적지만 -> dasom
    # case2) 출발지 + 목적지 -> dasom
    # case3) 출발지 + 목적지 + 시간 -> dasom(출발시간), suhyeon(도착시간)
    # case4) 출발지 + 목적지 + 날짜
    # case5) 출발지 + 목적지 + 날짜 + 시간

    # DEP에서 ARR로 가는 DATE DEP_TIME 에 출발하는 버스 예약해줘
    bus_list_1=[]
    for i in range(800):
        start, end = get_route()
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
        
        bus_list_1.append(start + '에서 ' + end + random.choice(['로', '으로'])+' 가는 ' + date + ' ' +dep_time + '에 출발하는 버스 ' + random.choice(reserve) + random.choice(ending))

    #DEP 출발 ARR 도착 출발 시각은 DEP_TIME
    bus_list_2=[]
    for i in range(800):
        start, end = get_route()
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
        
        bus_list_2.append(start + ' 출발 ' + end + ' 도착' + ' 출발 시각은 ' + date + ' ' + dep_time)
    
    #DEP 출발 ARR 도착 도착 시각은 DEP_TIME
    bus_list_2=[]
    for i in range(800):
        start, end = get_route()
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
        
        bus_list_2.append(start + ' 출발 ' + end + ' 도착' + ' 도착 시각은 ' + dep_time)

    # DEP에서 ARR 버스 DATE DEP_TIME 예약할래
    bus_list_3=[]
    for i in range(800):
        start, end = get_route()
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
        
        bus_list_3.append(start + '에서 ' + end + random.choice([' ', ' 차 ', ' 버스 ', ' 티켓 ']) + date + ' ' + dep_time)

    # ARR 로 가는 버스 DATE ARR_TIME 안에 도착하는 걸로 예약해줘
    bus_list_4=[]
    for i in range(1000):
        start, end = get_route()
        arr_time = random.choice([get_atime_hour(), get_atime_hourmin(), get_atime_exp_hour(), get_atime_exp_hourmin()])

        bus_list_4.append(end + random.choice(['로 가는 ', ' 도착하는 ', '으로 가는 ']) + random.choice(['', '버스 ', '티켓 ', '차 '])+ date + ' ' + arr_time + random.choice([' 안에 ', '내에 ', '까지 ']) + random.choice(['도착하는거 예약해줘', '도착하는 걸로', '도착하는 걸로 예약할래']))

    # DEP에서 ARR로 가는 버스 예약할거야. ARR_TIME 안에 도착하는 걸로.
    bus_list_5=[]
    for i in range(800):
        start, end = get_route()
        arr_time = random.choice([get_atime_hour(), get_atime_hourmin(), get_atime_exp_hour(), get_atime_exp_hourmin()])

        bus_list_5.append(start+ random.choice(['에서 ', '출발해서 ', ' 출발 ']) + end + random.choice(['로 가는 ', '으로 가는 ', '도착하는 ', ' 도착 ']) + random.choice([' ', ' 차 ', ' 버스 ', ' 티켓 ']) + random.choice(reserve) + random.choice(['할거야.', '할래.', '해줘.'])+ arr_time + random.choice(['에 도착', '에 도착하는 걸로', '안에 도착', '뒤에 도착하는걸로', '도착', '내에 도착']))

    # ARR_TIME 뒤에 도착하는 DEP에서 ARR가는 버스 예약할거야
    bus_list_6=[]
    for i in range(800):
        start, end = get_route()
        arr_time = random.choice([get_atime_hour_later(), get_atime_min_later(), get_atime_hourmin_later()])

        bus_list_6.append(arr_time + random.choice(['에 도착하는', '에 도착']) + start + '에서 ' + end + '가는 버스') 

    # DEP_TIME에 출발해서 ARR 도착하는 버스
    bus_list_7=[]
    for i in range(800):
        start, end = get_route()
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
        
        bus_list_7.append(date + ' ' + dep_time +  random.choice(['에 출발해서', '출발']) + end + random.choice(['도착하는 버스', '도착', '도착할거야']))
    
    bus_list=bus_list_1+bus_list_2+bus_list_3+bus_list_4+bus_list_5+bus_list_6+bus_list_7

    return bus_list

