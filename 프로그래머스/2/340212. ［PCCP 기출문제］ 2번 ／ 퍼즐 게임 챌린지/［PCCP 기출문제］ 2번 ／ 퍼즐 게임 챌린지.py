def cal(lv,diffs, times, limit):
    cnt = 0
    for i in range(len(diffs)):
        diff = diffs[i]
        if diff>lv:
            cnt += (times[i]+times[i-1])*(diff-lv)
            
        cnt += times[i]
        
        if cnt>limit:
            return False
        
    return True
            
        
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