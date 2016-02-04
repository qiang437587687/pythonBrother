#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('常用内建模块')


# datatime  处理日期和时间的标准库

# 获取当前时间
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间

dtt = datetime(2016, 2, 4, 10, 59)
print(dtt)
print(type(dtt))
print(dtt.timestamp())   # 打印出时间戳 如果有小数 那么小数表示的是毫秒数, 别的语言可能是整数表示
                         # 所以遇到时候对应的除以1000 就对应上了.


tt = 1429417200.0
print(datetime.fromtimestamp(tt))  # 反向的转换
print(datetime.utcfromtimestamp(tt))  # 标准转换 (上面的转换是根据系统做出的东八区时间)


# str转换为datetime 注意转换后的时间是没有时区的

cday = datetime.strptime('2016-01-04 11:05:04', '%Y-%m-%d %H:%M:%S')
print(cday)


# datetime 转换为 str
print(datetime.now().strftime('%a %H:%M:%S'))


# 时间的加减
from datetime import  timedelta
nowt = datetime.now()
print(now)

print(now + timedelta(hours=10)) # 十小时以后
print(now + timedelta(days=1000)) # 1000天以后


# 本地时间转换为 UTC 时间
from datetime import timezone

tz_utc_8 = timezone(timedelta(hours=8))

nowww = datetime.now()
print(nowww)
dt = now.replace(tzinfo=tz_utc_8)  # 强制转换为UTC+8:00  # 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区


#  时区转换

# 获取UTC时间并且强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

# 将UTC时间转换为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
