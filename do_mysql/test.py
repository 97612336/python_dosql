import datetime
import extract


time=datetime.datetime.utcnow()

print(time)
print(type(time))
new_time=time.strftime("%Y-%m-%d %H:%M:%S")
print(new_time)
print(type(new_time))

# ncmbot.login()