#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
    return best_score
