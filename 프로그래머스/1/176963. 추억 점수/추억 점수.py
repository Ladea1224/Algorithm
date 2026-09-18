def solution(name, yearning, photo):
    keyVal = {}
    for i in range(len(name)):
        keyVal[name[i]] = yearning[i]
        
    answer = []
    for arr in photo:
        score = 0;
        for person in arr:
            score += keyVal.get(person,0) 
        answer.append(score)
            
    return answer