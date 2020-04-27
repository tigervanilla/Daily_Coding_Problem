# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def minimum_rooms_required(intervals):
    arr = []    # to store all the time in sorted order
    for interval in intervals:
        arr.append((interval[0], 'S'))  # S means start time
        arr.append((interval[1], 'E'))  # E means end time
    arr.sort(key=lambda x: x[0])
    cnt, rooms = 0, 0
    for time in arr:
        if time[1] == 'S':
            cnt += 1
        elif time[1] == 'E':
            cnt -= 1
        rooms = max(rooms, cnt)
    return rooms


def minimum_rooms_required2(intervals):
    intrvls = intervals.copy()
    i, n = 0, len(intrvls)
    rooms = 0
    for i in range(n):
        if intrvls[i] == None:
            continue
        for j in range(i+1, n):
            if intrvls[j] == None:
                continue
            if (intrvls[i][1] < intrvls[j][0]) or (intrvls[i][0] > intrvls[j][1]):
                intrvls[j] = None
        intrvls[i] = None
        rooms += 1
    return rooms


def minimum_rooms_required3(intervals):
    timesheet = [0]*86400   # 86400=total seconds in a day
    for intrvl in intervals:
        timesheet[intrvl[0]] += 1
        timesheet[intrvl[1]+1] -= 1
    rooms = 0
    for i in range(1, 86400):
        timesheet[i] += timesheet[i-1]
        rooms = max(rooms, timesheet[i])
    return rooms


# Driver Code:
intervals1 = [(30, 75), (0, 50), (60, 150)]
intervals2 = [(30, 75), (0, 50), (60, 150), (50, 60), (90, 100)]
print(minimum_rooms_required(intervals1), minimum_rooms_required(intervals2))
print(minimum_rooms_required2(intervals1), minimum_rooms_required2(intervals2))
print(minimum_rooms_required3(intervals1), minimum_rooms_required3(intervals2))
