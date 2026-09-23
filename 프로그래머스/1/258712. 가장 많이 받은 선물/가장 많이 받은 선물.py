def solution(friends, gifts):
    idx = {}
    for i,friend in enumerate(friends):
        idx[friend] = i
        
    n = len(friends)
    sen = [0]*n
    rec = [0]*n
    matrix = [[0]*n for _ in range(n)]
    
    for gift in gifts:
        a,b = gift.split()
        ia,ib = idx[a],idx[b]
        sen[ia]+=1
        rec[ib]+=1
        matrix[ia][ib]+=1
    
    next = [0]*n
    for i in range(n):
        for j in range(i+1,n):
            ij,ji = matrix[i][j],matrix[j][i]
            if ij>ji:
                next[i]+=1
            elif ji>ij:
                next[j]+=1
            else:
                iScore,jScore = sen[i]-rec[i],sen[j]-rec[j]
                if iScore>jScore:
                    next[i]+=1
                elif jScore>iScore:
                    next[j]+=1
                
    return max(next)