from heapq import heappop, heappush

def heuristic_manhattan(a, b):
    
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_drone(grid, start, goal):
   
    open_list = [(0, start[0], start[1])]
    came_from = {}
    cost_so_far = {(start[0], start[1]): 0}

    while open_list:
        current_cost, x, y = heappop(open_list)
        if (x, y) == goal:
            break
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == '#': 
                    continue
                try:
                    new_cost = cost_so_far[(x, y)] + int(grid[nx][ny])
                except ValueError:
                    continue 
                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    priority = new_cost + heuristic_manhattan((nx, ny), goal)
                    heappush(open_list, (priority, nx, ny))
                    came_from[(nx, ny)] = (x, y)
    
    
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from.get(current, None)
        if current is None:
            return None  
    path.append(start)
    return path[::-1]


grid = [
    ['S', '2', '3'],
    ['1', '#', '4'],
    ['5', 'G', '2']
]


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i, j)
            grid[i][j] = '0'  
        elif grid[i][j] == 'G':
            goal = (i, j)
            grid[i][j] = '0'  


path = a_star_drone(grid, start, goal)
print("Jalur Drone:", path)  
