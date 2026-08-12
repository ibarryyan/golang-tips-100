"""时区处理与 zoneinfo/pytz"""

from datetime import datetime

# Python 3.9+ 使用 zoneinfo（推荐）
try:
    from zoneinfo import ZoneInfo

    tz_sh = ZoneInfo("Asia/Shanghai")
    tz_ny = ZoneInfo("America/New_York")

    # 创建带时区的 datetime
    dt_sh = datetime(2024, 6, 15, 14, 30, tzinfo=tz_sh)
    print(f"上海时间: {dt_sh}")

    # 时区转换
    dt_ny = dt_sh.astimezone(tz_ny)
    print(f"上海转纽约: {dt_ny}")

    # UTC 转换
    dt_utc = dt_sh.astimezone(ZoneInfo("UTC"))
    print(f"上海转 UTC: {dt_utc}")

    # 当前各时区时间
    now_sh = datetime.now(tz_sh)
    now_ny = datetime.now(tz_ny)
    print(f"现在上海: {now_sh}")
    print(f"现在纽约: {now_ny}")

except ImportError:
    print("zoneinfo 不可用，请使用 Python 3.9+ 或安装 backports.zoneinfo")

# 使用 pytz（Python 3.8 及以下）
try:
    import pytz

    tz_sh_pytz = pytz.timezone("Asia/Shanghai")
    tz_ny_pytz = pytz.timezone("America/New_York")

    # pytz 需要 localize 方法
    dt_sh = tz_sh_pytz.localize(datetime(2024, 6, 15, 14, 30))
    dt_ny = dt_sh.astimezone(tz_ny_pytz)
    print(f"pytz 上海转纽约: {dt_ny}")
except ImportError:
    print("pytz 未安装")

# 获取可用时区数量
try:
    tzs = zoneinfo.available_timezones() if 'zoneinfo' in dir() else {}
    print(f"可用时区数: {len(tzs)}")
except Exception:
    pass
