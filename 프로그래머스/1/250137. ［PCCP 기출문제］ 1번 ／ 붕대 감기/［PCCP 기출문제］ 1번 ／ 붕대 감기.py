"""
def solution(bandage, health, attacks):
    maxH = health
    timeB,upB,bonusB = bandage[0],bandage[1],bandage[2]
    currA,keep = 0,0
    
    for i in range(1,attacks[-1][0]+1):
        if i == attacks[currA][0]:
            health -= attacks[currA][1]
            if health<=0: return -1
            keep = 0
            currA += 1
        else:
            health = min(health+upB,maxH)
            keep += 1
            if keep == timeB:
                health = min(health+bonusB,maxH)
                keep = 0
    return health
"""
#풀이2: 시간 간격 이용. 어차피 attack 사이에서 일어나는 일은 정해져 있으므로
def solution(bandage, health, attacks):
    maxH = health
    timeB,upB,bonusB = bandage
    prev = 0
    
    for timeA,damageA in attacks:
        width = timeA-prev-1
        if width>0:
            health+= (width*upB) + (width//timeB)*bonusB
            health = min(health,maxH)
            
        health -= damageA
        if health<=0: return -1
    
        prev = timeA
        
    return health
        
    