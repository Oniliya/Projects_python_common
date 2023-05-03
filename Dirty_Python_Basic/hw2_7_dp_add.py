# ДЗ до среды (ну вообще до следующего воскресенья):

# 2. На шахматной доске расположить 8 ферзей так, чтобы они не били друг друга
# приложить хотя бы один вариант такой расстановки

def put_queen():
    return None


def main():
    board=[]
    for i in range(8):
        board.insert(i,[0,0,0,0,0,0,0,0])
        print(board[i])

    put_queen(i,j)

main()
















# import numpy as np
 
 
# def under_attack(col, queen):
#     return col in queen or \
#            any(abs(col - x) == len(queen) - i for i, x in enumerate(queen))
 
 
# def solve(n):
#     solutions = [[]]
#     for row in range(n):
#         solutions = [solution + [i + 1]
#                      for solution in solutions
#                      for i in range(n)
#                      if not under_attack(i + 1, solution)]
#     return solutions
 
 
# def queens(size):
#     result = np.array(solve(size))
#     for i in result:
#         np.sort(i)
#     for answer in result:
#         print(''.join(map(str, answer)))


# queens(8)

