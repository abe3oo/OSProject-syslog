import re
import sys
from datetime import timedelta, datetime
import chardet



#list zakhire sazi ...
generallist = []
lstTime = []

'''
def parse_log_file(file_path):
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            # Customize the regular expression based on your log format
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (.+)', line)
            if match:
                timestamp, message = match.groups()
                logs.append({'timestamp': timestamp, 'message': message})
    return logs
'''
#l = parse_log_file("C:\Users\Amir\Downloads\Compressed\syslog_ywcp")

'''
with open('D:\Daneshgah\OSL\PJ\syslog_ywcp\syslogg.txt', 'r') as f:
    lanes = f.read().split('\n')
'''
file_path = 'D:\Daneshgah\OSL\PJ\syslog_ywcp\syslogg.txt'
#find kardan file incode

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

print('detect encode ...') #print loading
fileencode = detect_encoding(file_path)
#......................

#joda kardan har khat va gozashtan har kodom toye list
def line_spliter():
    with open(file_path, 'r', encoding=fileencode) as f:
        lines = []
        for line in f:
            data = line.split()
            lines.append(data)
        return lines
        #print(lines)
print('loading data ...') #print loading
generallist = line_spliter()
print(generallist)

def time_extractor(gnlist):
    #def tabdil mah be number
    def month_generator(month):
        if month == 'Jan':
            return 1
        elif month == 'Feb':
            return 2
        elif month == 'Mar':
            return 3
        elif month == 'Apr':
            return 4
        elif month == 'May':
            return 5
        elif month == 'Jun':
            return 6
        elif month == 'Jul':
            return 7
        elif month == 'Aug':
            return 8
        elif month == 'Sep':
            return 9
        elif month == 'Oct':
            return 10
        elif month == 'Nov':
            return 11
        elif month == 'Dec':
            return 12
    for i in gnlist:
        linetime = datetime(1000,month_generator(i[0]),int(i[1]),int(i[2].split(':')[0]),int(i[2].split(':')[1]),int(i[2].split(':')[2]))
        lstTime.append(linetime)
    #print(lstTime)




def search_by_Date_and_Time(gnlist,tlist,stime,etime):
    Tlisthere = tlist
    gnlistnew = []
    def generate_time_range(start_time, end_time, step=timedelta(hours=1)):
        current_time = start_time
        time_list = []  # لیست برای ذخیره خروجی ساعت‌ها به صورت اشیاء datetime
        while current_time <= end_time:
            time_list.append(current_time)
            current_time += step
        return time_list
    start_time = stime  # زمان شروع
    end_time = etime   # زمان پایان
    time_step = timedelta(seconds=1)  # گام زمانی، در اینجا 30 دقیقه
    result_time_list = generate_time_range(start_time, end_time, step=time_step)
    
    index_search = []
    for times in result_time_list:
        for timestlist in Tlisthere:
            if times == timestlist:
                index_search.append(Tlisthere.index(timestlist))
                Tlisthere[Tlisthere.index(timestlist)] = '0'
    for i in index_search:
        gnlistnew.append(gnlist[i])
    return gnlistnew
    





print('. . . . .')
print('--help for see commands!')
print('. . . . .')
while True:
    act = input('-- enter your command: ')

    if act == '--help':
        print('\n-d ==> search by date and clock')
        print('-e ==> search by event type')
        print('-m ==> search in message text')
        print('-c ==> exit')

    elif act == '-d':
        time_extractor(generallist)
        startdate = 0
        enddate = 0
        print('input your start date. month, day, hour, min, sec')
        print('example: 3 1 11 54 12')
        try:
            x, y, a, b ,c = list(map(int, input('input >> ').split()))
            startdate = datetime(1000,x,y,a,b,c)
            print('input your end date. month, day, hour, min, sec')
            x, y, a, b ,c = list(map(int, input('input >> ').split()))
            enddate = datetime(1000,x,y,a,b,c)
        except:
            print('invalid format.')

        if startdate != 0:
            print('Loading ...')
            lst1 = []
            lst1 = search_by_Date_and_Time(generallist,lstTime,startdate,enddate)
            if len(lst1) >= 1:
                print(lst1)
            else:
                print('No data found !!!')

    elif act == '-m':
        

        pass

        
    elif act == '-c':
        exit()

