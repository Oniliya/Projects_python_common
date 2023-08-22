# Структурное программирование:
# __
# Трассировка пути в лабиринте:
# __
# Описание: Имеется двумерный массив, представляющий лабиринт, где '0' - это проход, а '1' - это стена. 
# Начальная и конечная точки заданы. Необходимо определить путь от начальной до конечной точки.
# Почему это структурное программирование: Задача может быть решена с помощью последовательных шагов, ветвлений 
# (проверка на наличие стены или уже посещенной клетки) и циклов (для обработки всех возможных направлений движения).

def is_valid(x: int, y: int, maze):
    if (x<0) or (y<0) or (x>=len(maze)) or (y>=len(maze[0])):
        return False
    if maze[x][y] == '1':
        return False
    return True

def wave_alg(maze, start_point, end_point):
    queue = [start_point]
    visited = set()
    visited.add(start_point)
    width = len(maze)
    height = len(maze[0])

    while queue:
        x,y, distance_length = queue.pop(0)

        if (x,y) == end_point:
            return distance_length
        
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_x, new_y = x+dx, y+dy

            if is_valid(new_x, new_y, maze) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, distance_length+1))
    
    return -1            

if __name__ == "__main__":
    maze = [
        ['0', '1', '0', '0', '0'],
        ['0', '1', '0', '1', '0'],
        ['0', '0', '0', '1', '0'],
        ['0', '1', '0', '0', '0'],
        ['0', '1', '0', '1', '0']
    ]
 

    distance_length = wave_alg(maze, start_point=(0, 0, 0), end_point=(4,4))
    print(f"path length = {distance_length}")