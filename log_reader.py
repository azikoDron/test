import datetime

for i in range(1, 31):
    if i < 10:
        time_start = '19:0' + str(i)
    if i >= 10:
        time_start = '19:' + str(i)

time_end = '19:30'

all_status = {
    'status_1': 0,
    'status_2': 0, 'status_3': 0,
    'status_4': 0, 'status_5': 0
     }
with open(r'C:\Username\any.log') as f:
    reader = f.readlines()
    for read in reader:
        if time_start in read:
            if 'status_1' in read:
                all_status['status_1'] = int(read[15:])
            if 'status_2' in read:
                all_status['status_2'] = int(read[15:])
            if 'status_3' in read:
                all_status['status_3'] = int(read[15:])
            if 'status_4' in read:
                all_status['status_4'] = int(read[15:])
            if 'status_5' in read:
                all_status['status_5'] = int(read[15:])

        if time_start in read:
            if 'status_1' in read:
                all_status['status_1'] = int(read[15:])
            if 'status_2' in read:
                all_status['status_2'] = int(read[15:])
            if 'status_3' in read:
                all_status['status_3'] = int(read[15:])
            if 'status_4' in read:
                all_status['status_4'] = int(read[15:])
            if 'status_5' in read:
                all_status['status_5'] = int(read[15:])