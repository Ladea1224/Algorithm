def cal(lv,diffs, times, limit):
    cnt = 0
    for i in range(len(diffs)):  # for diff,time in zip(diffs,times) 도 가능.
        diff = diffs[i]
        if diff>lv:
            cnt += (times[i]+times[i-1])*(diff-lv)
            
        cnt += times[i]
        
        if cnt>limit:
            return False
        
    return True

"""
#현재 관점: 가능=e, 불가능=s. s와 e가 1 차이 나는 지점이 경계이므로, 해당 시점에서의 e 가 정답

#다른 관점: 탐색한 곳 다시 포함 X, 전 범위 탐색 후(= s와 e가 역전 된 후) answer 가 정답.
while s <= e:
    lv = (s + e) // 2
    if cal(lv, diffs, times, limit):
        answer = lv
        e = lv - 1
    else:
        s = lv + 1
"""

def solution(diffs, times, limit):
    
    s,e = 0,max(diffs)
    while e-s!=1:
        lv = (s+e)//2
        possible = cal(lv,diffs, times, limit)
        if possible:
            e = lv
        else:
            s = lv

    return e
