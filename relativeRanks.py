def ranks(score):
    sol_arr = [0 for i in range(len(score))]
    score1 = []
    score1 = sorted(score, reverse=True)
    print(score1)
    
    for item in score:
        if item == score1[0]:
            sol_arr[score.index(item)] = "Gold Medal"
        elif item == score1[1]:
            sol_arr[score.index(item)] = "Silver Medal"
        elif item == score1[2]:
            sol_arr[score.index(item)] = "Bronze Medal"
        else:
            sol_arr[score.index(item)] = score1.index(item)+1
    return sol_arr

    
print(ranks([1,2,3,4,5]))