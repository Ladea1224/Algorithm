def solution(players, callings):
    ranks = {}
    for i in range(len(players)):
        ranks[players[i]] = i
    
    for call in callings:
        rank = ranks[call]
        forwardName = players[rank-1]

        players[rank-1], players[rank] = players[rank], players[rank-1]
        
        ranks[call] -= 1;
        ranks[forwardName] += 1;
        

        
    return players