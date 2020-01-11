#!/usr/bin/env python3

# import sys #for line in sys.stdin.readlines():
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



# input lines singlehandedliy
# convert to nodes
class board:
    def __init__(self, sudoku):
        # empy array of nodes
        self.sudoku = np.array([[node(0, x, y) for x in range(9)] for y in range(9)])
        self.orig = sudoku.copy()

        # replacing instances we know of
        for y, col in enumerate(sudoku):
            for x, i in enumerate(col):
                if i != 0:
                    self.sudoku[y, x].set_value(i)

    # for printing without nodes
    def __repr__(self):
        # return str(self.sudoku)
        return str(np.array([[x.value for x in y] for y in self.sudoku]))

    # iterating the values
    def _nodes(self):
        return self.sudoku.flatten()

    # returning only the values
    def vals(self):
        return np.array([[x.value for x in y] for y in self.sudoku])

    # get node-row of sudoku
    def get_row(self, y):
        return self.sudoku[y,:]

    # get values in row
    def get_row_vals(self, y):
        return [n.value for n in self.get_row(y)]


    # get node-column of sudoku
    def get_col(self, x):
        return self.sudoku[:,x]

    # get values in col
    def get_col_vals(self, x):
        return [n.value for n in self.get_col(x)]


    # get node-square of sudoku
    def get_square(self, x, y):
        min_x = (x//3) * 3
        min_y = (y//3) * 3
        max_x = min_x + 3
        max_y = min_y + 3
        return self.sudoku[min_y:max_y, min_x:max_x].flatten()

    # get values in square
    def get_square_vals(self, x, y):
        return [n.value for n in self.get_square(x, y)]


    # get 3d array of sudoku, with possibilities being the 3rd dimension
    def get_3d(self):
        # call function to see possibilities, and return as 3d array
        pass


    # generate the possible answers to each node
    def _get_possible(self):
        for n in self._nodes():
            # if node already has a value, skip it
            if n.value:
                continue

            row = self.get_row_vals(n.y)
            col = self.get_col_vals(n.x)
            square = self.get_square_vals(n.x, n.y)
            n.possible = set([]) # reset possible values

            # iterate the possibilities
            for i in range(1,10):
                if i not in np.array((row, col, square)).flatten():
                    n.add_possible(i)

            # print(n.possible)

            if len(n.possible) < 1:
                raise ValueError('Sudoku cannot be solved')


    def _add_singles(self):
        # add all with single possible value
        for cols in self.sudoku:
            for n in cols:
                if len(n.possible) == 1:
                    n.set_value(n.possible.pop

    def location_safe(self, val, x, y):
        row = get_row(y)
        col = get_col(x)
        square = get_square(x, y)
        return all([val not in area for area in [row, col, square]])


    def bruce_force(self):
        pass 


    def solve(self):
        prev = None
        while not np.array_equal(prev, self.vals()):
            print('SWITCH!')
            prev = self.vals()
            self._get_possible()
            self._add_singles()



class node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

        self.possible = set([]) #possible values if unset

    def __repr__(self):
        # return str(self.value)
        return "node({})".format(str(self.value))


    def set_value(self, val):
        self.value = val
        self.possible = set([])

    # def unset_value(self):
    #     self.value = 0

    def add_possible(self, no):
        self.possible.add(no)

    # def rm_possible(self, no):
    #     self.possible.remove(no)






if __name__ == '__main__':

    convert()
