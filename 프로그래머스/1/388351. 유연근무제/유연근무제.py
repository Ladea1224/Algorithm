def getAdmit(sd):
    admit = []
    for time in sd:
        if time%100 < 50:
            admit.append(time+10)
            continue
        h = (time//100) + 1
        m = ((time+10)%100)%60
        admit.append(h*100 + m)
    return admit
    
def solution(schedules, timelogs, startday):
    admit = getAdmit(schedules)
    DOW = [ (i if i<=7 else i-7) for i in range(startday,startday+7)]
    answer = 0
    for i,case in enumerate(timelogs):
        out = False
        for j,time in enumerate(case):
            if DOW[j] == 6 or DOW[j] == 7: continue
            if(time > admit[i]):
                out = True
                break
        if not out: answer += 1
    
    return answer