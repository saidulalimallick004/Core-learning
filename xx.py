import datetime

# Get the current date and time
now = datetime.datetime.now()

# Print the current date and time
print("Current date and time:", now)

# Format the date and time (optional)
# You can customize the format using directives like %Y, %m, %d, %H, %M, %S
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")  # Example: YYYY-MM-DD HH:MM:SS
print("Formatted date and time:", formatted_now)


# Just the current date:
current_date = datetime.date.today()
print("Current date:", current_date)
formatted_date = current_date.strftime("%Y-%m-%d") #Example: YYYY-MM-DD
print("Formatted date:", formatted_date)


# Just the current time:
current_time = now.time()
print("Current time:", current_time)
formatted_time = current_time.strftime("%H:%M:%S") #Example: HH:MM:SS
print("Formatted time:", formatted_time)


# For UTC time:

import datetime

now_utc = datetime.datetime.utcnow()
print("Current UTC date and time:", now_utc)
formatted_now_utc = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
print("Formatted UTC date and time:", formatted_now_utc)


#To handle timezones (more complex):
import datetime
import pytz  # You might need to install pytz: pip install pytz

# Get a specific timezone (e.g., India Standard Time)
ist = pytz.timezone("Asia/Kolkata")

# Get the current time in that timezone
now_ist = datetime.datetime.now(ist)
print("Current IST date and time:", now_ist)
formatted_now_ist = now_ist.strftime("%Y-%m-%d %H:%M:%S %Z%z") #Includes timezone info
print("Formatted IST date and time:", formatted_now_ist)

