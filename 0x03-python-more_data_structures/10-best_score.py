#!/usr/bin/python3
def best_score(a_dictionary):
    count = 0
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        if count == 0:
            best_score = value
        if value > best_score:
            best_score = value
    if best_score == -1:
        return None
    return best_score
