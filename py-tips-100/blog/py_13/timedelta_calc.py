"""timedelta 计算时间差"""

import time
from datetime import datetime, timedelta

now = datetime.now()

# 加减时间
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_two_hours = now + timedelta(hours=2)

print(f"明天: {tomorrow}")
print(f"昨天: {yesterday}")
print(f"下周: {next_week}")
print(f"两小时后: {in_two_hours}")

# 计算两个日期的差
start = datetime(2024, 1, 1)
end = datetime(2024, 6, 15)
diff = end - start
print(f"相差: {diff.days} 天")
print(f"总秒数: {diff.total_seconds()}")
print(f"总小时: {diff.total_seconds() / 3600}")

# 计时场景
t0 = time.time()
time.sleep(0.5)
t1 = time.time()
elapsed = t1 - t0
print(f"耗时: {elapsed:.3f} 秒")

# timedelta 格式化
td = timedelta(seconds=3661.5)
print(f"timedelta 默认格式: {td}")

total_seconds = int(td.total_seconds())
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"格式化: {hours}时{minutes}分{seconds}秒")

# timedelta 比较
td1 = timedelta(hours=1)
td2 = timedelta(minutes=90)
print(f"1小时 > 90分钟? {td1 > td2}")  # False
print(f"1小时 < 90分钟? {td1 < td2}")  # True

# .days 只返回整天数（不含小数）
td3 = timedelta(days=1.9)
print(f"days: {td3.days}")  # 1
print(f"total_seconds: {td3.total_seconds()}")  # 164160.0
