from datetime import date, timedelta
from datetime import datetime
today = date.today()
yesterday = today - timedelta(days = 1)
print(today)
print(yesterday)
presentday = datetime.now()  # or presentday = datetime.today()
# # Get Yesterday
yesterday = presentday - timedelta(1)
tomorrow = presentday + timedelta(1)
Yesterday =  yesterday.strftime('%d-%m-%Y')
Today = presentday.strftime('%m-%d-%Y')
today_date = datetime.today().strftime('%Y-%m-%d')
print(today_date)
print(Today)

# this method insert date
from datetime import datetime
today_date = datetime.today().strftime('%Y-%m-%d')
presentday = datetime.now()  # or presentday = datetime.today()
# # Get Yesterday
# yesterday = presentday - timedelta(1)
# tomorrow = presentday + timedelta(1)
# Yesterday =  yesterday.strftime('%d-%m-%Y')
Today = presentday.strftime('%m-%d-%Y')