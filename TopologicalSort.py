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


1 - graph = defaultdict(list) Creates an adjacency list. Each key is
    a course, and its value is a list of dependent courses.

2 - indegree = [0] * numCourses Tracks how many prerequisites each
    course has. We're going to fill the indegree list with 0s meaning,
    initially, we assume no course has any prerequisites.

    In a directed graph, the indegree of a node is the number of edges
    coming into it. Here, it means how many prerequisite courses must be
    completed before you can take that course. Example: if course 3 requires
    1 and 2 first, indegree[3] = 2.

    If numCourses = 4 then indegree = [0, 0, 0, 0]
    This means:

    Course 0 has 0 prerequisites
    Course 1 has 0 prerequisites
    Course 2 has 0 prerequisites
    Course 3 has 0 prerequisites (for now)

3 - course and prereq are indexes

    graph = {0:[], 1:[], 2:[], 3:[]}
    indegree = [0,0,0,0]

    Since indegree[0] requires 0 prerequisites, indegree[1] will be 1 because
    course[1] depends on 0 -> course[2] depends on 0, so we also add 1 ->
    course 3 depends on 1, so we add 1 -> course 3 depends on 1, so we add 2
    again

    course 0 is the prerequisite, so thats why the first 0 is not a 1, its not
    a dependant course and we add 1s to dependant courses

4 - [i for i in range(numCourses) if indegree[i] == 0] Go through all course
    IDs from 0 to numCourses-1 and collect only those whose indegree value
    is 0

    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    graph = {0:[1,2], 1:[3], 2:[3]}
    indegree = [0,1,1,2]

    queue = deque([0]) We wrap that list inside a deque (double-ended queue)
    Because it allows fast removal from the left (popleft()) and fast addition
    to the right (append())

5 - while queue is TRUE because queue = [0]
    - current = queue.popleft() says current = 0, queue = []
    - order.append(current) says order = [0]

6 - for neighbor in graph[current]: says Iterate over graph[0] = [1,2]:
    - neighbor = 1 → indegree[1] goes 1 → 0 because of the decrement

    - → indegree now [0,0,1,2]
    - → since it's now 0 → queue.append(1)

    - neighbor = 2 → indegree[2] goes 1 → 0
    - → indegree now [0,0,0,2]
    - → queue.append(2)

    --- End of loop 1 ---

    queue = [1,2]
    order = [0]
    indegree = [0,0,0,2]

    --- That was loop 1, this is loop 2 ---

    - Pop: current = 1, queue = [2]
    - Append: order = [0,1]

    - Iterate over graph[1] = [3]
    - neighbor = 3 → indegree[3] goes 2 → 1

    --- End of loop 2 ---

    queue = [2]
    order = [0,1]
    indegree = [0,0,0,1]

    --- Loop 3 ---

    - Pop: current = 2, queue = []
    - Append: order = [0,1,2]

    - Iterate over graph[2] = [3]
    - neighbor = 3 → indegree[3] goes 1 → 0
    - indegree[3] == 0 → add to queue

    --- End of loop 3 ---

    queue = [3]
    order = [0,1,2]
    indegree = [0,0,0,0]

    --- Loop 4 ---

    - Pop: current = 3, queue = []
    - Append: order = [0,1,2,3]
    - graph[3] = [] (no neighbors)

    --- End of loop 4 ---

    queue = []
    order = [0,1,2,3]
    indegree = [0,0,0,0]



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

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))