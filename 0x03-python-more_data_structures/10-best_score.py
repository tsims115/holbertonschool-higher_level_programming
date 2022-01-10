#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = -1
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > best_score or best_score == -1:
            best_score = value
    return best_score
