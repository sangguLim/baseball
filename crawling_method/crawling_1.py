import requests

data = {'MIME Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
        'leId': 1,
        'srId': 0,
        'seasonId': 2021,
        'gameId': '20210711HHSK0'
       } 
res = requests.post('https://www.koreabaseball.com/ws/ Schedule.asmx/GetScoreBoardScroll', data=data)

# <Response [200]> 이 뜨면 정상 접속
print(res)