"""

PROBLEM


You are given two lists — start and end — where start[i] and end[i]
represent the start and end times of an activity.

You can only perform one activity at a time.
Find the maximum number of activities that can be performed by a
single person, assuming a person can start the next activity only
after the previous one finishes.



STEPS


1 - 



"""

def max_activities(start, end):
    n = len(start)
    activities = list(zip(start, end)) # Pair each start time with its end time
    activities.sort(key=lambda x: x[1]) # Sort activities by their ending time

    count = 1
    last_end_time = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_end_time:
            count += 1
            last_end_time = activities[i][1]
    return count

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print("Maximum number of activities:", max_activities(start, end))