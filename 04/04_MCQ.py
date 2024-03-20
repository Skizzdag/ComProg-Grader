def MCQ(solve, answer):
    score = 0
    if len(solve) == len(answer):
        for i in range(len(solve)):
            if solve[i] == answer[i]:
                score += 1
    else:
        return print("Incomplete answer")
    return print(score)
MCQ(input(),input())