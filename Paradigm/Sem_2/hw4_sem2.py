# **Структурное программирование:

# Трассировка пути в лабиринте:**
# __
# Задание: Создайте функцию, которая принимает двумерный массив (лабиринт) и начальную и конечную точки. 
# Функция должна возвращать путь от начальной до конечной точки или сообщение, что путь невозможен.
# Входные данные:
# Двумерный массив размера MxN, где '0' - это проход, а '1' - это стена.
# Координаты начальной и конечной точки.
# Выходные данные:
# Массив координат пути или сообщение об ошибке.

from collections import deque

def find_path(maze, start_point, end_point):
    rows = len(maze)
    cols = len(maze[0])

    visited = [[False]*cols for _ in range(rows)]

    prev = [[None]*cols for _ in range(rows)]

    offsets = [(1,0),(-1,0),(0,1),(0,-1)]

    queue = deque([start_point])
    visited[start_point[0]][start_point[1]]= True

    while queue:
        x, y = queue.popleft()

        if (x,y) == end_point:
            path=[]
            while (x,y )!= start_point:
                path.append_point((x,y))
                x,y = prev[x][y]
            path.append_point(start_point)
            path.reverse()
            return path

        for  dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if (0<=nx<rows) and (0<=ny<cols) and (maze[nx][ny]=='0') and (not visited[nx][ny]):
                queue.append_point((nx, ny))
                visited[nx][ny] = True
                prev[nx][ny] = (x, y)
    
    return None


if __name__ == "__main__":
    maze = [
        ['0', '1', '0', '0', '0'],
        ['0', '1', '0', '1', '0'],
        ['0', '0', '0', '1', '0'],
        ['0', '1', '0', '0', '0'],
        ['0', '1', '0', '1', '0']
    ]
    start_point = (0, 0)
    end_point = (4, 4)

    path = find_path(maze, start_point, end_point)

    if path:
        print ("path exist")
        for x, y in path:
            print(f"({x}, {y})")
    else:
        print("path dont exist")

