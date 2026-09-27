"""
기존
def solution(survey, choices):
    s = "RTCFJMAN"
    score = {x:0 for x in s}
    cToS = {i:(0,4-i) for i in range(1,5)} | {i:(1,i-4) for i in range(5,8)}
    
    for surv,cho in zip(survey,choices):
        idx,plus = cToS[cho]
        score[surv[idx]] += plus
    
    answer = ""
    for i in range(0,len(s),2):
        l,r = s[i],s[i+1]
        if score[l]==score[r]:
            answer += l
            continue
        else:
            answer += l if score[l]>score[r] else r
    
    return answer
"""

#리팩토링
def solution(survey, choices):
    s = "RTCFJMAN"
    score = {x:0 for x in s}
    
    for surv,cho in zip(survey,choices):
        if cho<4:
            score[surv[0]] += 4-cho
        if cho>4:
            score[surv[1]] += cho-4
    
    answer = ""
    for i in range(0,len(s),2):
        l,r = s[i],s[i+1]
        answer += l if score[l]>=score[r] else r
    
    return answer