from typing import List, Tuple


def best_student2(scores: List[Tuple[str, int]]) -> str:
    highest_scoring_pair = ("",0)
    for name, score in scores:
        if score > highest_scoring_pair[1]:
            highest_scoring_pair = name, score
    
    return highest_scoring_pair[0]



def best_student(scores: List[Tuple[str, int]]) -> str:
    best_student, best_score = "", 0

    for name, score in scores:
        if score > best_score:
            best_student, best_score = name, score
    
    return best_student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
