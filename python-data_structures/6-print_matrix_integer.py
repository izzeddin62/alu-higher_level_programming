#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            if i:
                for j in i:
                    if i.index(j) == len(i) - 1:
                        print('{:d}'.format(j))
                        break
                    print('{:d}'.format(j), end=" ")
            else:
                print()
