#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best_score = 0
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
    return best_score
