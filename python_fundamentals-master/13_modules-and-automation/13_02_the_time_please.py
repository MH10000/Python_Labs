# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
from datetime import datetime

# Importing an object from the datetime module to get the current date and time
date_time_now = datetime.now()

# dd/mm/YY H:M:S
dt_string = date_time_now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)