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



#  namedtuple 这是一个函数用来自定义一个tuple对象 规定了tuple的
#  元素个数并且可以用属性 而不是索引来引用tuple
#  可以很党鞭的根据属性来引用又具有tuple的不变性.

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)   # 1
print(p.y)   # 2


    # 用来表示一个圆

Circle = namedtuple('Circle', ['x', 'y', 'r'])

cir = Circle(3, 4, 5)
print(cir.x, cir.y, cir.r)


# deque  实现高效的插入和删除操作的双向列表 适用于队列和栈

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# deque 实现了list 的append() 和pop() 还支持appendleft() 和popleft()
q.popleft()
print(q)


# defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])  # 这个其实是不存在的 那么返回的是默认值 'N/A'
# 注意这个默认值是在调用函数的时候返回的创建的时候传入到defaultdict里面的
# 除了在key不存在的时候返回默认值 其他的行为和dict 是一样的.


# OrderDict   有序的Dict

from collections import OrderedDict

df = dict([('a', 1), ('c', 3), ('b', 2)])
df1 = dict
print('无序的df', df)  # 现在的这个df 是无序的

od = OrderedDict([('1', 1), ("2", 2)])
print(od)

od['4'] = '4'
od['5'] = '5'
print('注意od 的顺序是按照插入的顺序进行排列的不是ke本身的顺序: ',od)

print(1 if '6' in od else 0)   # 这语法不错!


#  counter 简单的计数器

from collections import Counter

c = Counter()
for ch in 'Programming':
    c[ch] = c[ch] + 1

print(c)  # Counter({'r': 2, 'g': 2, 'm': 2, 'n': 1, 'i': 1, 'a': 1, 'P': 1, 'o': 1})









