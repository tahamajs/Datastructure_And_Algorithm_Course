# tmp = input()
input_numbers = int(input())

def is_in_range(time1,time2,main_time):
    if time1 <= main_time <= time2:
        return True
    else:
        return False


def time_inventor(timee):
    timet , ampm = timee.split(' ')
    hour , minute = timet.split(':')
    if ampm == 'PM' and hour != '12':
        hour = int(hour) + 12
    if ampm == 'AM' and hour == '12':
        hour = 0



    return int(hour) * 60 + int(minute)


lis = []
for u in range(input_numbers):
    ilist = []
    main_time = input()
    main_time = time_inventor(main_time)
    num = int(input())
    for _ in range(num):
        timee = input()
        time1 , time2 = ([time_inventor(' '.join(timee.split(' ')[0:2])),time_inventor(' '.join(timee.split(' ')[2:4]))])
        ilist.append(str(int(time1 <= main_time <= time2)))
    lis.append(''.join(ilist))

print('\n'.join(lis))
