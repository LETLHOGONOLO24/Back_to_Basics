"""

PROBLEM


You are given two lists — start and end — where start[i] and end[i]
represent the start and end times of an activity.

You can only perform one activity at a time.
Find the maximum number of activities that can be performed by a
single person, assuming a person can start the next activity only
after the previous one finishes.



STEPS


1 - activities = list(zip(start, end)) Combines both start and end
    lists into pairs for each activity, like:

    [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]

2 - activities.sort(key=lambda x: x[1]) Sorts the activities by their
    end time. The greedy idea here is always choose the activity that
    finishes earliest — this leaves more room for the next one.

    [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]

    Same in this example, but in other cases order might change.

3 - count = 1 We can always choose the first activity after sorting.
4 - last_end_time = activities[0][1] Keeps track of the ending time
    of the last selected activity. Initially, it's the end time of the
    first activity (which ends earliest).

5 - for i in range(1, n): Iterate through all remaining activities.
6 - if activities[i][0] >= last_end_time: If the start time of the current
    activity is greater or equal to the end time of the previously selected
    activity → we can perform it.

7 - count += 1 and last_end_time = activities[i][1] - When selected, increment
    the count and update the last ending time.




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