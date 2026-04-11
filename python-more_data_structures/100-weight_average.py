#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight = sum(weight for weight, _ in my_list)
    if total_weight == 0:
        return 0

    weighted_sum = sum(weight * score for weight, score in my_list)
    return weighted_sum / total_weight
