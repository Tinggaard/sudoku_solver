# import sys #for line in sys.stdin.readlines():
import numpy as np
import sys

def get_solution():
    chksum = 0
    for i in range(9):
        n = int(sys.stdin.readline())
        if n < 123456789 or n > 987654321:
            sys.exit(1)
        chksum  = ((chksum + n + 8) * 23652789) % 9345692873
    return chr((chksum % 47)+95)




# input lines singlehandedliy
# convert to nodes
class board:
    def __init__(self, sudoku):
        # empy array of nodes
        self.sudoku = np.array([[node(0, x, y) for x in range(9)] for y in range(9)])
        self.size = self.sudoku.shape

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

            if len(n.possible) < 1:
                raise ValueError('Sudoku cannot be solved')


    def _add_singles(self):
        # add all with single possible value
        for cols in self.sudoku:
            for n in cols:
                if len(n.possible) == 1:
                    n.set_value(n.possible.pop())


    def loop(self):
        prev = None
        while not np.array_equal(prev, self.vals()):
            prev = self.vals()
            self._get_possible()
            self._add_singles()




    # def _add_pairs(self):
    #     change = True
    #     c = 0
    #     while change:
    #         # update everything
    #         c += 1
    #         change = False
    #         self._get_possible()
    #
    #
    #         # iterate all nodes in sudoku
    #         for n in self._nodes():
    #             # if node already has a value, skip it
    #             if n.value:
    #                 continue
    #
    #             print('NEW NODE')
    #
    #             row = self.get_row(n.y)
    #             col = self.get_col(n.x)
    #             square = self.get_square(n.x, n.y)
    #
    #             # iterating each row, col and square seperately
    #             for item in (row, col, square):
    #                 test = n.possible.copy()
    #                 print('TESTING WITH: ', (n.x, n.y), test)
    #
    #                 # skip if value or self
    #                 for indicy in item:
    #                     if indicy.value or (indicy.x == n.x and indicy.y == n.y):
    #                         continue
    #
    #
    #                     print('possible: ', indicy.possible)
    #                     # subtract set of possible of iterated
    #                     test -= indicy.possible
    #                     print('set after: ', test, '\n')
    #
    #                 if len(test) < 1:
    #                     raise ValueError('Sudoku cannot be solved')
    #
    #                 # add if only possible answer in type (row, col, square)
    #                 elif len(test) == 1:
    #                     print('added something my dudes...', (n.x, n.y))
    #                     n.set_value(test.pop())
    #                     change = True
    #                     break
    #
    #
    #
    #                 print('________________')
    #
    #     print(c)






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



# re:    print\("[1-9.]{9}"\)
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


l1 = [2, 0, 3, 0, 0, 0, 7, 0, 4]
l2 = [0, 9, 1, 2, 7, 4, 5, 0, 3]
l3 = [0, 6, 7, 3, 5, 9, 2, 0, 1]
l4 = [7, 0, 0, 6, 0, 3, 0, 4, 5]
l5 = [5, 3, 4, 0, 1, 7, 6, 2, 8]
l6 = [0, 8, 0, 0, 2, 0, 9, 0, 7]
l7 = [9, 1, 0, 5, 3, 6, 4, 7, 2]
l8 = [3, 4, 5, 0, 9, 0, 0, 0, 6]
l9 = [0, 0, 2, 0, 0, 1, 0, 0, 9]
sudoku = np.array([l1,l2,l3,l4,l5,l6,l7,l8,l9])

sudoku2 = \
[[2, 8, 0, 7, 5, 0, 9, 3, 0],
 [5, 9, 6, 2, 3, 8, 1, 4, 7],
 [3, 1, 7, 9, 4, 6, 8, 5, 2],
 [0, 2, 3, 6, 9, 4, 5, 0, 0],
 [0, 7, 5, 8, 1, 2, 3, 9, 0],
 [8, 4, 9, 3, 7, 5, 6, 0, 1],
 [7, 5, 2, 1, 6, 9, 4, 0, 0],
 [0, 0, 8, 4, 2, 0, 7, 0, 0],
 [4, 3, 1, 5, 8, 7, 2, 6, 9]]




if __name__ == '__main__':

    s = board(sudoku2)

    print('input')
    print(s)

    s.loop()

    print('\nafter single possibilities')
    print(s)
