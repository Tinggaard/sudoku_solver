#!/usr/bin/evn python3

import numpy as np
import sys


def get_solution(l) -> str:
    chksum = 0
    for i in l:
        if 0 in i:
            raise Exception('Sudoku not solved...')

        n = int(''.join(map(str, i))) # convert from list to single number


        if n < 123456789 or n > 987654321:
            sys.exit(1)
        chksum  = ((chksum + n + 8) * 23652789) % 9345692873
    return chr((chksum % 47)+95)


def convert():
    flag = ''
    for b in range(24):
        print(b)
        arr = np.zeros([9, 9], dtype=np.intc)
        for i in range(9):
            n = list(sys.stdin.readline().replace('.', '0')[:-1]) # exclude newline
            row = list(map(int, n))
            arr[i] = row

        sud = board(arr)
        sud.solve()
        flag += get_solution(sud.vals())

    print(flag)



def get_row(arr, y) -> list:
   return arr[y,:]

def get_col(arr, x) -> list:
   return arr[:,x]

def get_square(arr, x, y) -> list:
   min_x = (x//3) * 3
   min_y = (y//3) * 3
   max_x = min_x + 3
   max_y = min_y + 3
   return arr[min_y:max_y, min_x:max_x].flatten()

def solve_singles(arr):
    prev = None
    while not np.array_equal(prev, arr):
        prev = arr.copy()

        for val in range(arr.size):
            y = val // arr.shape[0]
            x = val % arr.shape[0]
            
            # if already set
            if arr[y, x]:
                continue
            
            possible = []
            for i in range(1, 10):
                s = get_square(arr, x, y)
                c = get_col(arr, x)
                r = get_row(arr, y)

                if i not in np.array((s, c, r)):
                    possible.append(i)

            if len(possible) == 1:
                arr[y, x] = possible.pop()


def solved(arr) -> bool:
    return 0 not in arr






def backtrack(arr) -> bool:
    for i in range(arr.size):
        row = i // arr.shape[0]
        col = i % arr.shape[0]

        # if arleady set
        if arr[row, col]:
            continue

        for val in range(1,10):
            s = get_square(arr, col, row)
            c = get_col(arr, col)
            r = get_row(arr, row)

            if val not in np.array((s, c, r)):
                arr[row, col] = val
                if solved(arr):
                    print('Solved the sudoku!')
                    return True
                else:
                    if backtrack(arr):
                        return True
        return False
    print('backtrack')
    arr[row, col] = 0

first = \
[[2, 0, 3, 0, 0, 0, 7, 0, 4],
 [0, 9, 1, 2, 7, 4, 5, 0, 3],
 [0, 6, 7, 3, 5, 9, 2, 0, 1],
 [7, 0, 0, 6, 0, 3, 0, 4, 5],
 [5, 3, 4, 0, 1, 7, 6, 2, 8],
 [0, 8, 0, 0, 2, 0, 9, 0, 7],
 [9, 1, 0, 5, 3, 6, 4, 7, 2],
 [3, 4, 5, 0, 9, 0, 0, 0, 6],
 [0, 0, 2, 0, 0, 1, 0, 0, 9]]

arr = np.array(first)


if __name__ == '__main__':
    backtrack(arr)
    print(solved(arr))











