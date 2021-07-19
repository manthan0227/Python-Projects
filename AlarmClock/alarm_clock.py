from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set : HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

print("Setting up alarm.....")
while True:
    now = datetime.now()
    cur_hour = now.strftime("%I")
    cur_minute = now.strftime("%M")
    cur_second = now.strftime("%S")
    cur_period = now.strftime("%p")
    if(alarm_period == cur_period):
        if alarm_hour == cur_hour:
            if alarm_minute == cur_minute:
                if alarm_second == cur_second:
                    print("Wake up!.....")
                    playsound('alarm.mp3')
                    break

