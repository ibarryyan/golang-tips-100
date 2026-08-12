"""时间戳与 datetime 互转"""

import time
from datetime import datetime, timezone

# 获取当前时间戳
timestamp = time.time()
print(f"当前时间戳: {timestamp}")

# datetime 转时间戳
dt = datetime(2024, 6, 15, 14, 30, 0)
ts = dt.timestamp()
print(f"datetime 转时间戳: {ts}")

# 时间戳转 datetime
dt2 = datetime.fromtimestamp(ts)
print(f"时间戳转 datetime: {dt2}")

# 使用 UTC 避免时区问题
dt_utc = datetime.now(timezone.utc)
ts = dt_utc.timestamp()
dt_back = datetime.fromtimestamp(ts, tz=timezone.utc)
print(f"UTC datetime: {dt_back}")

# 毫秒级时间戳（常见于 API）
ms = int(time.time() * 1000)
print(f"毫秒时间戳: {ms}")

# 毫秒时间戳转 datetime
ms = 1718430600000
dt_ms = datetime.fromtimestamp(ms / 1000)
print(f"毫秒转 datetime: {dt_ms}")

# 时间戳转可读字符串
ts = 1718430600
readable = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
print(f"可读时间: {readable}")
