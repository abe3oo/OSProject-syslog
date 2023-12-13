import re
import chardet
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
with open('D:\Daneshgah\OS\PJ\syslog_ywcp\syslogg.txt', 'r') as f:
    lanes = f.read().split('\n')
'''
file_path = 'D:\Daneshgah\OS\PJ\syslog_ywcp\syslogg.txt'
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']
fileencode = detect_encoding(file_path)
def line_spliter():
    with open(file_path, 'r', encoding=fileencode) as f:
        lines = []
        for line in f:
            data = line.split()
            lines.append(data)
        return lines
        #print(lines)
print(line_spliter())
def search_by_Date_and_Time(mylog_List):
    day = ''
    m = ''
    

    for line in mylog_List:
        day = line[1]
        m = line[0]





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
        print('a')
    elif act == '-c':
        exit()

