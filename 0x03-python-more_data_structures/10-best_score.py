#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = -1
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
    if best_score == -1:
        return None
    return best_score
