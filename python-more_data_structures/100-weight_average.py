#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_sum = 0
    weight_sum = 0
    for i in my_list:
        weighted_sum += i[0] * i[1]
        weight_sum += i[1]
    return weighted_sum / weight_sum
