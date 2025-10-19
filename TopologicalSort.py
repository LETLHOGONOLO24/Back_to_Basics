"""


PROBLEM


You are given the number of courses numCourses and a list of
prerequisite pairs.
Each pair [a, b] means that to take course a, you must first
complete course b.
Return a possible order to finish all the courses. If it's
impossible (due to a cycle), return an empty list.

Example Input
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

Expected Output
[0, 1, 2, 3]
Explanation:
You can take course 0 first, then 1 and 2 (both depend on 0),
and finally 3 (depends on 1 and 2).


STEPS


1 - 



"""

from collections import defaultdict, deque

def findOrder(numsCourses, prerequisites):

    # Step 1: Build adjacency list for the graph
    graph = defaultdict(list)

    # indegree[i] = number of prerequisites for course i
    indegree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    # Step 2: Start with courses that have no prerequisites
    # (indegree = 0)
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []

    # Step 3: Process the queue
    while queue:
        current = queue.popleft()
        order.append(current)

        # Decrease indegree for neighbors
        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            # if a course now has no prerequisitses, add it to queue
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: If we could take all courses, return order, else return []
    return order if len(order) == numCourses else []
