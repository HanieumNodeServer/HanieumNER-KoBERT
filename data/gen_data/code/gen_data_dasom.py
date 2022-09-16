from gen_data import *
import random

def dasom():
    reserve = ["예약", "예매" ,"티켓 발행", "티켓 예약", "티켓 예매","발권"]
    ending = [' 해 줘',' 해 주세요', '하고 싶어','할래','해','하려 하는데 표 있어?', '하고 싶어요','할게요', '할게', ' 부탁합니다', ' 가능해?' , " 가능한가요"]
    
    ################ 시나리오 1(일반 문장) #############################
    # case 1) 목적지만 얘기하는 상황 
    # ex1_1) ARR, ARR으로, ARR으로 갈래 등 
    route_list1_1 = []
    ending_word = ['', '으로', '으로 갈래', '으로 가고 싶어' ,'행', ' 도착', ' 가는 버스', ' 갈래', ' 가고 싶어' , ' 갈래요', ' 도착으로' , ' 갈거야']
    for i in range(900):
        start, end = get_route()
        
        route_list1_1.append(end + random.choice(ending_word))

    # ex1_2) 도착지가 ARR인 버스 예약해줘 
    route_list1_2 = []
    starting_word = ['도착지는 ', '목적지는 ', '' , '도착지가 ', '목적지가 ', '도착은 ']
    for i in range(900):
        start, end = get_route()
        route_list1_2.append(random.choice(starting_word) + end +"인 버스 " + random.choice(reserve) + random.choice(ending))

    #case 2) 출발지와 목적지를 얘기하는 상황 
    # ex2_1) DEP에서 ARR
    route_list2_1 = []
    for i in range(900):
        strat, end = get_route()

        route_list2_1.append(start + "에서 " + end)

    # ex2_2) 여기서 ARR로
    starting = ['여기서 ', '내 위치 기반으로 ', '가장 가까운 역에서 ', '가까운 역에서 ', '여기에서 ']
    route_list2_2 = []
    for i in range(900):
      start, end = get_route()

      route_list2_2.append(random.choice(starting) + end + random.choice(ending_word))

    # ex2_3) 여기서 ARR로 가는 버스 예약해줘
    route_list2_3 = []
    for i in range(900):
      start, end = get_route()

      route_list2_3.append(random.choice(starting) + end + random.choice(['으로 가는 버스 ', '로 가는 버스 ']) + random.choice(reserve) + random.choice(ending)) 

    # ex2_4) DEP 출발 ARR 도착하는 버스
    route_list2_4 = []
    for i in range(900):
      start, end = get_route()
      route_list2_4.append(start + random.choice(['에서 ', ' 출발 ', '에서 출발 ', '에서 출발해서 ']) + end + random.choice(['로 ', '으로 ', '으로 도착 ', '로 도착하는',' 도착인 ', '도착하는 ', '행 버스', '으로 가는 ', '로 가는 ']) + random.choice(reserve) + random.choice(ending))
    
    # ex2_5) ARR 가는데 출발은 DEP
    route_list2_5 = []
    word = ending_word  + [' 가는데', ' 갈 건데' , ' 가려고 하는데', ' 가고 싶은데']
    for i in range(900):
      start, end = get_route()
      route_list2_5.append(end + random.choice(word) + ', 출발은 ' +random.choice(starting))

    # ex2_6) ARR 가는데 출발지는 DEP인 버스 예약하려고 해
    route_list2_6 = []
    for i in range(900):
      start, end = get_route()
      route_list2_6.append(end + random.choice(word) + random.choice([' 출발은', ' 출발지는 ', ' 출발지가 ']) + start +'인 버스' + random.choice(reserve) + random.choice(ending))

    
    # case 3) (출발지) + 목적지 + 출발시간
    # ex3_1) DEP에서 출발해서 ARR로 도착하는 DEP_TIME 버스 예약할래
    route_list3_1 = []
    for i in range(900):
        start, end = get_route()
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
        
        route_list3_1.append(start + random.choice(['에서 ', ' 출발 ', '에서 출발 ', '에서 출발해서 ']) + end + random.choice(['로 ', '으로 ', '으로 도착 ', '로 도착하는',' 도착 인 ',  '도착하는 ', '도착 ']) + dep_time + ' 버스' + random.choice(reserve) + random.choice(ending))

    # ex3_2) ARR로 도착하는 DEP_TIME에 출발하는 버스, DEP 출발할거야
    route_list3_2 = []
    for i in range(900):
        start, end = get_route()
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
        
        route_list3_2.append(end +random.choice(['로 ', '으로 ', '으로 도착 ', '로 도착하는',' 도착 인 ', '도착하는 ', '행 ']) + dep_time + '에 출발하는 버스 ' + start + random.choice(['에서 ', '출발 ', '에서 출발하는 ']) + random.choice(reserve) + random.choice(ending))

    # ex3_3) DEP_TIME에 DEP 출발하는 ARR가는 버스
    route_list3_3 = []
    for i in range(900):
        start, end = get_route()
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
      
        route_list3_3.append(dep_time + '에 ' + start + random.choice(['에서 ', '출발 ', '에서 출발하는 ', ' ']) + end + random.choice(['로 ', '으로 ', '으로 도착 ', '로 도착하는',' 도착 인 ', ' 도착하는 ', '행 버스', '으로 가는 ', '로 가는 '])+ random.choice(reserve) + random.choice(ending))

    # ex3_4) DEP_TIME에 ARR가는 버스
    route_list3_4 = []
    for i in range(900):
        start, end = get_route()
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
      
        route_list3_4.append(dep_time + '에 ' + end + random.choice(['로 ', '으로 ', '으로 도착 ', '로 도착하는',' 도착 인 ', ' 도착하는 ', '행 버스', '으로 가는 ', '로 가는 ']) + random.choice(reserve) + random.choice(ending))

    route = route_list1_1 + route_list1_2 + route_list2_1 + route_list2_2 + route_list2_3 + route_list2_4 + route_list2_5 + route_list2_6 +route_list3_1 + route_list3_2 + route_list3_3 + route_list3_4

    
    ################## 시나리오 2(변경 사항 발생하는 경우) #############
    reject=['','아니 ','음.. ','음.. 아니 ','아니야 ','잠시만 ', '잠깐만 ']
    change=['바꿀게','수정해줘','바꿔줘','바꿔 주세요','수정할게','변경해주세요', '변경해줘', '변경 부탁합니다', '수정할게요']
    starting = ['여기서 가장 가까운 역으로 ', '내 위치 기반으로 ', '가장 가까운 역으로 ', '가까운 역으로 ', '여기로 ', '내 위치 기준으로 ']
    dep_change=['에서 출발하는 걸로 ', '에서 출발로 ','출발하는 버스로 ',' 출발 버스로 ' ]
    arr_change=['도착하는 걸로 ', '로 도착하는 ', '도착하는 버스로 ', ' 도착 버스로 ' ]
    
    # ex1) 아니 출발지는 DEP로 바꿀게
    route_list1 = []
    for i in range(900):
        start, end  = get_route()
        
        route_list1.append(random.choice(reject) + '출발지는 ' + start + random.choice(change)) 
    
    # ex2) 아니, 내 위치로 바꿀게 
    route_list2 = []
    for i in range(900):
        start, end = get_route()
    
        route_list2.append(random.choice(starting) + random.choice(change))

    # DEP에서 출발하는걸로 바꿀게
    route_list3 = []
    for i in range(900):
        start, end = get_route()
        
        route_list3.append(start + random.choice(dep_change) + random.choice(change))
    
    # 아니 도착지는 ARR로 바꿀게
    route_list4 = []
    for i in range(900):
        start, end  = get_route()
        
        route_list1.append(random.choice(reject) + '도착지는 ' + end + random.choice(change)) 

    # ARR로 도착하는걸로 바꿀게
    route_list5 = []
    for i in range(900):
        start, end = get_route()
        
        route_list5.append(end + random.choice(arr_change) + random.choice(change))
    

    # 출발 시간이랑 날짜는 DATE DEP_TIME로 바꿀래
    route_list6 = []
    for i in range(900):
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])
        
        route_list6.append( "출발 시간이랑 날짜는 " + date + ' ' + dep_time + random.choice(['로 ', '으로 ',' 버스로 ']) + random.choice(change))

    # DATE DEP_TIME 출발로 바꿀래
    route_list7 = []
    for i in range(900):
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        dep_time = random.choice([get_dtime_hour(), get_dtime_hourmin(), get_dtime_exp_hour(), get_dtime_exp_hourmin(), get_dtime_hour_later(), get_dtime_min_later(), get_dtime_hourmin_later()])

        route_list5.append(date + ' ' + dep_time + random.choice(['출발하는 버스로 ', '출발로 ', ' 출발 버스로 ']) + random.choice(change))

    # 아니 ARR_TIME 도착으로
    route_list8 = []
    for i in range(900):
        date = random.choice([get_date(random.choice([0,4])), get_date_with_weeksday(), get_date_exp_int()])
        arr_time = random.choice([get_atime_hour(), get_atime_hourmin(), get_atime_exp_hour(), get_atime_exp_hourmin(), get_atime_hour_later(), get_atime_min_later(), get_atime_hourmin_later()])

        route_list8.append(random.choice(reject) + date + ' ' + arr_time + random.choice(['안에 ', '까지는 ']) + random.choice(arr_change) + random.choice(change))

    route2 = route_list1 + route_list2 + route_list3 + route_list4 + route_list5 + route_list6 + route_list7 + route_list8

    return route + route2
