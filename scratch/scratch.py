import datetime

today = datetime.date.today()
date_of_round = today + datetime.timedelta(days=7)
day = datetime.datetime.strptime(str(date_of_round), "%Y-%m-%d")
dow = day.day
print(dow)
