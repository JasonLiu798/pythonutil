#!/bin/env python
#-*- coding:utf-8 -*-
import datetime
import time
import calendar

'''
data formmats
'''
YYYY_MM_DD_HH_MM_SS="%Y-%m-%d %H:%M:%S"

def day_get(d):
   oneday = datetime.timedelta(days = 1 )
   day = d - oneday
   date_from = datetime.datetime(day.year, day.month, day.day, 0 , 0 , 0 )
   date_to = datetime.datetime(day.year, day.month, day.day, 23 , 59 , 59 )
   print '---' .join([ str (date_from), str (date_to)])


def week_get(d):
   dayscount = datetime.timedelta(days = d.isoweekday())
   dayto = d - dayscount
   sixdays = datetime.timedelta(days = 6 )
   dayfrom = dayto - sixdays
   date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0 , 0 , 0 )
   date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23 , 59 , 59 )
   print '---' .join([ str (date_from), str (date_to)])

'''
def getMonth(d):
   dayscount = datetime.timedelta(days = d.day)
   dayto = d - dayscount
   date_from = datetime.datetime(dayto.year, dayto.month, 1 , 0 , 0 , 0 )
   date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23 , 59 , 59 )
   print '---' .join([ str (date_from), str (date_to)])
'''


# def date2ts(dt, convert_to_utc=False):
#     '''
#     Converts a datetime object to UNIX timestamp in milliseconds.
#     '''
#     if isinstance(dt, datetime.datetime):
#         return dt.format
#         if convert_to_utc: # 是否转化为UTC时间
#             dt = dt + datetime.timedelta(hours=-8) # 中国默认时区
#         timestamp = total_seconds(dt - EPOCH)
#         return long(timestamp)
#     return dt

def ts2date(timestamp, convert_to_local=False):
    ''' Converts UNIX timestamp to a datetime object. '''
    if isinstance(timestamp, (int, long, float)):
        dt = datetime.datetime.utcfromtimestamp(timestamp)
        if convert_to_local: # 是否转化为本地时间
            dt = dt + datetime.timedelta(hours=8) # 中国默认时区
        return dt
    return timestamp

def getNow():
    return datetime.datetime.now()

def getNowTs():
    return date2ts(getNow())


def str2date(date_str,fmt=YYYY_MM_DD_HH_MM_SS):
    # return time.mktime(time.strptime(string, fmt))
    return datetime.datetime.strptime(date_str, fmt)
# d = ts2date(1356587335)
# print date2ts(d)

def str2ts(dtStr,fmt=YYYY_MM_DD_HH_MM_SS):
    timeArray = time.strptime(dtStr, fmt)
    return int(time.mktime(timeArray))

def date2str(dt,fmt=YYYY_MM_DD_HH_MM_SS):
    return dt.strftime(fmt)

#date to timestamp
def date2ts(dt):
    # dtStr = date2str(dt)
    return calendar.timegm(dt.utctimetuple())




'''
interval<0
    get month before
interval>0
    get month after
'''
def getMonth(interval):
    dayscount = datetime.timedelta(days=abs(interval)*30)
    # print dayscount,type(dayscount)
    if interval>0:
        dayto = getNow() + dayscount
    else:
        dayto = getNow() - dayscount
    return dayto
    # datetime.datetime(dayto.year, dayto.month, 1 , 0 , 0 , 0 )


def getMonthTS(interval):
    return date2ts(getMonth(interval))

def getMonthFirstDay(interval):
    pass



# print getMonthTS(-6)



'''
strTime = "2013-10-10 23:40:00"
# res = str2date()
print type(res),res

res = str2ts(strTime)
print type(res),res
'''
# res = ts2date(1381419600)
# print res
# print getMonth(-6)
# print getMonthTS(-6)

# d=getMonth(-6)
# print date2ts(d)

# print datetime.datetime.fromtimestamp(time.time())
# print datetime.datetime(2013, 8, 10, 11, 14, 50, 842812)







