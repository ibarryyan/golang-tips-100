"""datetime 模块基础操作"""

from datetime import datetime, date, time

# 获取当前时间和日期
now = datetime.now()
today = date.today()
print(f"当前时间: {now}")
print(f"今天: {today}")

# 创建指定日期时间
dt = datetime(2024, 6, 15, 14, 30, 0)
print(f"指定时间: {dt}")

# 访问各字段
print(f"年: {now.year}, 月: {now.month}, 日: {now.day}")
print(f"时: {now.hour}, 分: {now.minute}, 秒: {now.second}")

# datetime 转字符串
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print(dt.strftime("%Y年%m月%d日"))
print(dt.strftime("%Y/%m/%d %H:%M"))
print(dt.strftime("%A, %B %d, %Y"))

# 字符串转 datetime
dt2 = datetime.strptime("2024-06-15 14:30:00", "%Y-%m-%d %H:%M:%S")
print(f"从字符串解析: {dt2}")

dt3 = datetime.strptime("2024年06月15日", "%Y年%m月%d日")
print(f"中文日期解析: {dt3}")
