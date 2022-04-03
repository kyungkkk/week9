from datetime import datetime


now  = datetime.now()
nowDict={0:'월요일',1:'화요일',2:'수요일',3:'목요일',4:'금요일',5:'토요일',6:'일요일'}

comparison_date=input("시작날짜(연/월/일):")
date_to_compare = datetime.strptime(comparison_date, "%Y/%m/%d")

date_diff = now - date_to_compare

print(f"{now}부터 오늘{comparison_date}까지는 {date_diff.days}일이 지났습니다.\n")
print(nowDict[now.weekday()])