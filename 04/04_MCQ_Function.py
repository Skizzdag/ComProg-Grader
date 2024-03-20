def grade_mcq(sol, ans):
    score = 0
    if len(sol) == len(ans):
        for i in range(len(sol)):
            if sol[i] == ans[i]:
                score += 1
    else:
        return -1
    return score
exec(input())