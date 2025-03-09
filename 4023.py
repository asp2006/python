# بررسی زمان روز و تعیین خوشامدگویی
time_of_day = input("enter the time of day(morning, afternoon, evening, night):")
if time_of_day == "morning":
    print("Good morning! have a great start to your day.")
elif time_of_day == "afternoon":
    print("Good afternoon! hope your day is going well.")
elif time_of_day == "evening":
    print("Good evening! its time to unwind.")
elif time_of_day == "night":
    print("Good nigt! sweet dreams.")
else:
    print("Invalid time. Please enter morning, afternoon, evening, night.")