from datetime import datetime
import time

# Alarm times stored in a list
alarm_list = []

# Get alarm time from user
hour = int(input("Enter Hour (0-23): "))
minute = int(input("Enter Minute (0-59): "))
second = int(input("Enter Second (0-59): "))

# Store alarm time as a tuple
alarm_time = (hour, minute, second)

# Add tuple to list
alarm_list.append(alarm_time)

print("Alarm Set Successfully!")

while True:
    # Get current time as a tuple
    now = datetime.now()
    current_time = (now.hour, now.minute, now.second)

    print("Current Time:", current_time, end="\r")

    # Check whether current time is in the alarm list
    if current_time in alarm_list:
        print("\n⏰ Alarm Ringing!")
        print("Wake Up!")
        break

    time.sleep(1)
