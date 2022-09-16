<<<<<<< HEAD
import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
import re

def dateProcess(date):
    # 미리 지정할 수 있는 단어
    nows = ['오늘','금일', '지금','당장','빨리','현재','지금당장', '최대한빨리','가장빠른','가장빨리', '빨리빨리']
    tomorrow = ['익일','명일','내일']
    day_after_tomorrow = ['모레','내일모레']
    week = {'이번주':0 ,'다음주': 1, '다다음주': 2}
    
    # 현재 날짜 구하기
    today = datetime.datetime.now(timezone('Asia/Seoul'))

    # 경우의 수에 따른 regex 구하기
    date_regex2 = re.search(r'([가-힣|0-9|]{1,3})일*(후|뒤)', date) # 2) 경우의 수
    date_regex4 = re.search(r'(\d{1,2})월(\d{1,2})일', date) # 4) 경우의 수
    date_regex5 = re.search(r'(\d{1,2})일', date) # 5) 경우의 수
    date_regex6 = re.search(r'([가-힣])요일', date) #6) 경우의 수


    # 1)오늘 날짜 -> nows에 있는 거
    if date in nows:
        rd  = relativedelta(days = +0)

        return (today + rd).strftime('%Y%m%d')

    # 2)n일뒤, 일주일뒤, n주후, 보름뒤 등
    elif date_regex2 is not None:
        date_regex2 = date_regex2.group(1)

        if date_regex2 == '일주일':
            rd = relativedelta(days = +7)
        elif re.search(r'(\d{1,2})주', date_regex2) is not None:
            rd = relativedelta(weeks = +int(re.search(r'(\d{1,2})주', date_regex2).group(1)))
        elif re.search(r'(\d{1,2})일', date_regex2) is not None:
            rd = relativedelta(days = +int(re.search(r'(\d{1,2})일', date_regex2).group(1)))
        else:
            rd = relativedelta(days = +15) #일단 보름뒤만 해당(추가할 것 있으면 나중에 처리)

        return (today + rd).strftime('%Y%m%d')

    # 3)익일, 금일, 내일 등
    elif date in tomorrow:
        rd = relativedelta(days = +1)

        return (today + rd).strftime('%Y%m%d')

    elif date in day_after_tomorrow:
        rd = relativedelta(days = +2)

        return (today + rd).strftime('%Y%m%d')


    # 4)정확한 날짜 언급(n월 n일)
    elif date_regex4 is not None:
        m, d = int(date_regex4.groups()[0]), int(date_regex4.groups()[1])
        
        return datetime.datetime(today.year, m, d).strftime('%Y%m%d')

    # 5)일만 언급(n일) -> 월은 현재 달로 설정
    elif date_regex5 is not None:
        d = int(date_regex5.groups()[0])
        
        return datetime.datetime(today.year, today.month, d).strftime('%Y%m%d')

    # 6)요일 & 주+요일 변경 (수요일(가장 가까운 수요일 찾기), 이번주 월요일, 다음주 월요일, 다다음주 월요일등)
    elif date_regex6 is not None:
        w = 0

        for k in week.keys():
            if date.startswith(k):
                w = week.get(k)
                break
    
        today += relativedelta(weeks = +w)
        # 모든 기준일을 일요일로 설정
        today += relativedelta(weekday=SU(-1))

        date_regex6 = date_regex6.group(1)

        if date_regex6 == '월':
            rd = relativedelta(weekday=MO(1))
        elif date_regex6 == '화':
            rd = relativedelta(weekday=TU(1))
        elif date_regex6 == '수':
            rd = relativedelta(weekday=WE(1))
        elif date_regex6 == '목':
            rd = relativedelta(weekday=TH(1))
        elif date_regex6 == '금':
            rd = relativedelta(weekday=FR(1))
        elif date_regex6 == '토':
            rd = relativedelta(weekday=SA(1))
        else:
            rd = relativedelta(weekday=SU(2))
        
        return (today + rd).strftime('%Y%m%d')
    
    else:
        return ''

def timeProcess(time):
    # 현재 시간 구하기
    now = datetime.datetime.now(timezone('Asia/Seoul'))

    # 경우의 수에 따른 regex 구하기
    time_regex1 = re.search(r'^(\d{1,2})시(?!간)((\d{1,2})분|반)?', time) # 1) 경우의 수
    time_regex2 = re.search(r'((\d{1,2})시간)?((\d{1,2})분|반)?뒤', time) # 2) 경우의 수
    time_regex3 = re.search(r'^(아침|오전|새벽)((\d{1,2})시)((\d{1,2})분|반)?', time) # 3) 경우의 수
    time_regex4 = re.search(r'^(낮|오후|밤|저녁)((\d{1,2})시)((\d{1,2})분|반)?', time) # 4) 경우의 수

    # 1) 정확한 시간(n시n분, n시, n시반)
    if time_regex1 is not None:
        regex_h = time_regex1.group(1)
        if time_regex1.group(2) == '반':
            regex_m = '30'
        else:
            regex_m = time_regex1.group(3)

        h = int(regex_h)
        m = int(0 if regex_m is None else regex_m)
        
        return datetime.time(hour = h, minute = m).strftime('%H%M')

    # 2) n시간 뒤 or n분 뒤, n시간 n분
    elif time_regex2 is not None:
        regex_h = time_regex2.group(2)
        if time_regex2.group(3) == '반':
            regex_m = '30'
        else:
            regex_m = time_regex2.group(4)

        h = int(0 if regex_h is None else regex_h)
        m = int(0 if regex_m is None else regex_m)

        rd = relativedelta(hours = h, minutes = m)

        return (now + rd).strftime('%H%M')

    # 3) 새벽 n시, 아침 n시 n분, 오전 n시 반 등
    elif time_regex3 is not None:
        regex_h = time_regex3.group(3)
        if time_regex3.group(4) == '반':
            regex_m = '30'
        else:
            regex_m = time_regex3.group(5)
        
        h = int(regex_h)
        m = int(0 if regex_m is None else regex_m)

        return datetime.time(hour = h, minute = m).strftime('%H%M')

    # 4) 오후 n시, 저녁 n시 n분. 밤 n시 반
    elif time_regex4 is not None:
        regex_h = time_regex4.group(3)
        if time_regex4.group(4) == '반':
            regex_m = '30'
        else:
            regex_m = time_regex4.group(5)
        
        h = int(regex_h) + 12
        m = int(0 if regex_m is None else regex_m)

        return datetime.time(hour = h, minute = m).strftime('%H%M')

    else:
=======
import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
import re

def dateProcess(date):
    # 미리 지정할 수 있는 단어
    nows = ['오늘','금일', '지금','당장','빨리','현재','지금당장', '최대한빨리','가장빠른','가장빨리', '빨리빨리']
    tomorrow = ['익일','명일','내일']
    day_after_tomorrow = ['모레','내일모레']
    week = {'이번주':0 ,'다음주': 1, '다다음주': 2}
    
    # 현재 날짜 구하기
    today = datetime.datetime.now(timezone('Asia/Seoul'))

    # 경우의 수에 따른 regex 구하기
    date_regex2 = re.search(r'([가-힣|0-9|]{1,3})일*(후|뒤)', date) # 2) 경우의 수
    date_regex4 = re.search(r'(\d{1,2})월(\d{1,2})일', date) # 4) 경우의 수
    date_regex5 = re.search(r'(\d{1,2})일', date) # 5) 경우의 수
    date_regex6 = re.search(r'([가-힣])요일', date) #6) 경우의 수


    # 1)오늘 날짜 -> nows에 있는 거
    if date in nows:
        rd  = relativedelta(days = +0)

        return (today + rd).strftime('%Y%m%d')

    # 2)n일뒤, 일주일뒤, n주후, 보름뒤 등
    elif date_regex2 is not None:
        date_regex2 = date_regex2.group(1)

        if date_regex2 == '일주일':
            rd = relativedelta(days = +7)
        elif re.search(r'(\d{1,2})주', date_regex2) is not None:
            rd = relativedelta(weeks = +int(re.search(r'(\d{1,2})주', date_regex2).group(1)))
        elif re.search(r'(\d{1,2})일', date_regex2) is not None:
            rd = relativedelta(days = +int(re.search(r'(\d{1,2})일', date_regex2).group(1)))
        else:
            rd = relativedelta(days = +15) #일단 보름뒤만 해당(추가할 것 있으면 나중에 처리)

        return (today + rd).strftime('%Y%m%d')

    # 3)익일, 금일, 내일 등
    elif date in tomorrow:
        rd = relativedelta(days = +1)

        return (today + rd).strftime('%Y%m%d')

    elif date in day_after_tomorrow:
        rd = relativedelta(days = +2)

        return (today + rd).strftime('%Y%m%d')


    # 4)정확한 날짜 언급(n월 n일)
    elif date_regex4 is not None:
        m, d = int(date_regex4.groups()[0]), int(date_regex4.groups()[1])
        
        return datetime.datetime(today.year, m, d).strftime('%Y%m%d')

    # 5)일만 언급(n일) -> 월은 현재 달로 설정
    elif date_regex5 is not None:
        d = int(date_regex5.groups()[0])
        
        return datetime.datetime(today.year, today.month, d).strftime('%Y%m%d')

    # 6)요일 & 주+요일 변경 (수요일(가장 가까운 수요일 찾기), 이번주 월요일, 다음주 월요일, 다다음주 월요일등) -> 오늘이 금요일일때 다음주 월요일 구하는 알고리즘 다시 짜기!
    elif date_regex6 is not None:
        w = 0

        for k in week.keys():
            if date.startswith(k):
                w = week.get(k)
                break
    
        today += relativedelta(weeks = +w)
        
        date_regex6 = date_regex6.group(1)

        if date_regex6 == '월':
            rd = relativedelta(weekday=MO(1))
        elif date_regex6 == '화':
            rd = relativedelta(weekday=TU(1))
        elif date_regex6 == '수':
            rd = relativedelta(weekday=WE(1))
        elif date_regex6 == '목':
            rd = relativedelta(weekday=TH(1))
        elif date_regex6 == '금':
            rd = relativedelta(weekday=FR(1))
        elif date_regex6 == '토':
            rd = relativedelta(weekday=SA(1))
        else:
            rd = relativedelta(weekday=SU(1))

        return (today + rd).strftime('%Y%m%d')
    
    else:
        return ''

def timeProcess(time):
    # 현재 시간 구하기
    now = datetime.datetime.now(timezone('Asia/Seoul'))

    # 경우의 수에 따른 regex 구하기
    time_regex1 = re.search(r'^(\d{1,2})시(?!간)((\d{1,2})분|반)?', time) # 1) 경우의 수
    time_regex2 = re.search(r'((\d{1,2})시간)?((\d{1,2})분|반)?뒤', time) # 2) 경우의 수
    time_regex3 = re.search(r'^(아침|오전|새벽)((\d{1,2})시)((\d{1,2})분|반)?', time) # 3) 경우의 수
    time_regex4 = re.search(r'^(낮|오후|밤|저녁)((\d{1,2})시)((\d{1,2})분|반)?', time) # 4) 경우의 수

    # 1) 정확한 시간(n시n분, n시, n시반)
    if time_regex1 is not None:
        regex_h = time_regex1.group(1)
        if time_regex1.group(2) == '반':
            regex_m = '30'
        else:
            regex_m = time_regex1.group(3)

        h = int(regex_h)
        m = int(0 if regex_m is None else regex_m)
        
        return datetime.time(hour = h, minute = m).strftime('%H%M')

    # 2) n시간 뒤 or n분 뒤, n시간 n분
    elif time_regex2 is not None:
        regex_h = time_regex2.group(2)
        if time_regex2.group(3) == '반':
            regex_m = '30'
        else:
            regex_m = time_regex2.group(4)

        h = int(0 if regex_h is None else regex_h)
        m = int(0 if regex_m is None else regex_m)

        rd = relativedelta(hours = h, minutes = m)

        return (now + rd).strftime('%H%M')

    # 3) 새벽 n시, 아침 n시 n분, 오전 n시 반 등
    elif time_regex3 is not None:
        regex_h = time_regex3.group(3)
        if time_regex3.group(4) == '반':
            regex_m = '30'
        else:
            regex_m = time_regex3.group(5)
        
        h = int(regex_h)
        m = int(0 if regex_m is None else regex_m)

        return datetime.time(hour = h, minute = m).strftime('%H%M')

    # 4) 오후 n시, 저녁 n시 n분. 밤 n시 반
    elif time_regex4 is not None:
        regex_h = time_regex4.group(3)
        if time_regex4.group(4) == '반':
            regex_m = '30'
        else:
            regex_m = time_regex4.group(5)
        
        h = int(regex_h) + 12
        m = int(0 if regex_m is None else regex_m)

        return datetime.time(hour = h, minute = m).strftime('%H%M')

    else:
>>>>>>> afacd17016963c110f74a4bedc5a87604a932461
        return ''