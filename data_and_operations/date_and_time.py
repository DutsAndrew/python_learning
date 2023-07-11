import time

# current time

# this returns (year, month, day, hour, minute)
time_now = time.localtime(time.time())

# time.time() returns ticks
# localtime() converts the ticks to human readable values

current_time = time.localtime(time.time())
year,month,day,hour,minute = current_time[0:5]

print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute))

# Epoch time

seconds_since_epoch = time.time()
print(seconds_since_epoch) # 1689087917.9310327

time_sequence = time.gmtime()
print(time_sequence) # time.struct_time(tm_year=2023, tm_mon=7, tm_mday=11, tm_hour=15, tm_min=5, tm_sec=17, tm_wday=1, tm_yday=192, tm_isdst=0)

# Time in string

asc_time = time.asctime()
ctime = time.ctime()

print(asc_time) # Tue Jul 11 09:06:44 2023
print(ctime) # Tue Jul 11 09:06:44 2023

# Sleep
# Will halt program execution

print("Hello")
time.sleep(1) # delays program for 1 sec
print("World")
time.sleep(1) # delays program for 1 sec