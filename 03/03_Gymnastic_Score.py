def check_score(score):
    maxScore = 0
    minScore = 0
    #maxScore
    if score[0] > score[1] and score[0] > score[2] and score[0] > score[3]:
        maxScore = score[0]
    elif score[1] > score[2] and score[1] > score[3]:
        maxScore = score[1]
    elif score[2] > score[3]:
        maxScore = score[2]
    else:
        maxScore = score[3]
    #minScore
    if score[0] < score[1] and score[0] < score[2] and score[0] < score[3]:
        minScore = score[0]
    elif score[1] < score[2] and score[1] < score[3]:
        minScore = score[1]
    elif score[2] < score[3]:
        minScore = score[2]
    else:
        minScore = score[3]
    #avgScore
    score.remove(maxScore)
    score.remove(minScore)
    avgScore = round((score[0] + score[1]) / 2, 2)
    return print(avgScore)
check_score(list(map(float, input().split())))