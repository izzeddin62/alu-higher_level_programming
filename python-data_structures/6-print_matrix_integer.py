#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for j in i:
                if i.index(j) == len(i) - 1:
                    print('{}'.format(j))
                    break
                print('{}'.format(j), end=" ")
