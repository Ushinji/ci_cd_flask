import time
from datetime import datetime, timezone, timedelta


def epoch_msec():
    return int(time.time() * 1000)


def epoch_to_jst(epoch_msec):
    epoch = epoch_msec / 1000
    JST = timezone(timedelta(hours=+9), 'JST')
    return datetime.fromtimestamp(epoch, JST)
