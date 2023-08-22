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

def find_path(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    # массив для хранения посещенных ячеек
    visited = [[False]*cols for _ in range(rows)]

    # массив для хранения предыдущих ячеек
    prev = [[None]*cols for _ in range(rows)]

    #  смещения для переходов
    offsets = [(1,0),(-1,0),(0,1),(0,-1)]
    
    # ставим начальную точку в очередь
    queue = deque([start])
    
    # отмечаем начальную точку как псещенную
    visited[start[0]][start[1]]= True

    while queue:
        x, y = queue.popleft()

        # если текущая ячейка последняя, то строим путь
        if (x,y) == end:
            path=[]
            while (x,y )!= start:
                path.append((x,y))
                x,y = prev[x][y]
            path.append(start)
            path.reverse()
            return path

        # проверяем соседние ячейки
        for  dx, dy in offsets:
            nx, ny = x + dx, y + dy

            # проверяем, что ячейка внутри лабиринта и является проходом
            if (0<=nx<rows) and (0<=ny<cols) and (maze[nx][ny]=='0') and (not visited[nx][ny]):
                queue.append((nx, ny))
                visited[nx][ny] = True
                prev[nx][ny] = (x, y)

    # если путь не найден
    return None


if __name__ == "__main__":
    maze = [
        ['0', '1', '0', '0', '0'],
        ['0', '1', '0', '1', '0'],
        ['0', '0', '0', '1', '0'],
        ['0', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    start = (0, 0)
    end = (4, 4)

    path = find_path(maze, start, end)

    if path:
        print ("path exist")
        for x, y in path:
            print(f"({x}, {y})")
    else:
        print("path dont exist")