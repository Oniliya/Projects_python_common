# ДЗ до среды (ну вообще до следующего воскресенья):

# 2. На шахматной доске расположить 8 ферзей так, чтобы они не били друг друга
# приложить хотя бы один вариант такой расстановки

def put_queen(num_i, num_j :int ,my_list: list) ->list:
    for i in range(8):
        for j in range(8):
            if i== num_i or j== num_j:
                my_list[i][j]=1
            if j-num_j==i-num_i:
                my_list[i][j]=1
            if i-num_i==num_j-j:
                my_list[i][j]=1
            if i== num_i and j== num_j:
                my_list[i][j]=8
    return my_list

def print_board(my_board: list):
    for item in my_board:
        print(item)

def clear_board(my_board: list) -> list:
    new_board=[]
    for i in range(8):
        new_board.insert(i,[0,0,0,0,0,0,0,0])
    return new_board

import random

def main():
    board=[]
    for i in range(8):
        board.insert(i,[0,0,0,0,0,0,0,0])
    print_board(board)

    # for i in range(8):
    #     for j in range(8):
    #         if board[i][j]!=8 and board[i][j]!=1:
    #             put_queen(i,j,board)
    
    for _ in range(1000):
        i=random.randint(0,7)
        j=random.randint(0,7)
        if board[i][j] != 1 and board[i][j] !=8 :
            put_queen(i,j, board)

    print('------------------------')
    print_board(board)

    # board=clear_board(board)
    # print_board(board)


    # put_queen(5-1,5-1,board)
    # print('------------------------')
    # print_board(board)

main()




# my_list=[1,5,6,4,9,7]
# print(my_list)

# my_list[2]=190
# print(my_list)














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

