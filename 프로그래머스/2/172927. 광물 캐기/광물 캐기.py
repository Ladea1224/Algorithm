#완탐? 약 10^6
#그리디. 계획 좀 더 구체적으로 세우고 구현 시작 했어야 함.
"""
def solution(picks, minerals):
    mIdx = {"diamond":0, "iron":1, "stone":2}
    digCnt = sum(picks)*5
    minerals = minerals if len(minerals)<digCnt else minerals[:digCnt]
    
    scores = []
    for i in range(0,len(minerals),5): #i=0,5,...
        s,e = i, min(len(minerals),i+5)
        score = [0,0,0] #dia,iron,stone
        for j in range(s,e):
            mineral = minerals[j]
            score[mIdx[mineral]] += 1
        scores.append(score)
    
    scores.sort(key=lambda x: (-x[0],-x[1],-x[2])) #비싼 순 정렬

    tool = 0
    answer = 0
    for score in scores:
        
        while picks[tool]==0:
            tool += 1
        
        picks[tool] -= 1
        if tool==0:
            answer += sum(score)
        elif tool==1:
            answer += score[0]*5 + score[1] + score[2]
        else:
            answer += score[0]*25 + score[1]*5 + score[2]
        
    return answer
"""
        
#리팩토링. 
def solution(picks, minerals):
    digCnt = sum(picks)*5
    if len(minerals)>digCnt:            #삼항연산자, 리스트 컴프리헨션 등 억지로 X
        minerals = minerals[:digCnt]
    
    scores = []
    for i in range(0,len(minerals),5):  
        mineral = minerals[i:i+5] # 이미 미네랄 수 조정 했으므로 불일치 고려할 필요 X
        cnt0 = mineral.count("diamond") #굳이 인덱싱 사용않고 그냥 찾기, count 사용
        cnt1 = mineral.count("iron")
        cnt2 = mineral.count("stone")
        scores.append([cnt0,cnt1,cnt2]) 
    scores.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True) #reverse=True 옵션 사용
    
    tool = 0
    answer = 0
    for score in scores:
        
        while picks[tool]==0: #이미 미네랄 수 조정 했으므로 불일치 고려할 필요 X
            tool += 1
        
        picks[tool] -= 1
        if tool==0:
            answer += sum(score)
        elif tool==1:
            answer += score[0]*5 + score[1] + score[2]
        else:
            answer += score[0]*25 + score[1]*5 + score[2]
        
    return answer
    
            
    
        
        