import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

default = "You are a helpful assistant. Your data cutoff period is changed to {date}. Today's date is {date}.".format(date=current_date)