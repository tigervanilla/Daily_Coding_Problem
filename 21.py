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


# Driver Code:
intervals1 = [(30, 75), (0, 50), (60, 150)]
intervals2 = [(30, 75), (0, 50), (60, 150), (50, 60), (90, 100)]
print(minimum_rooms_required(intervals1), minimum_rooms_required(intervals2))
