from datetime import datetime

now  = datetime.now()
print("현재 :", now)	# 현재 : 2021-01-09 21:30:12.050111

date_to_compare = datetime.strptime("20201225", "%Y%m%d")
print("비교할 날짜 :", date_to_compare)	# 비교할 날짜 : 2020-12-25 00:00:00

date_diff = now - date_to_compare
print("차이 :", date_diff)