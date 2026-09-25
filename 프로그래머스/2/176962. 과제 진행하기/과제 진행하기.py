#반복문 내부에서의 순서 배치 혼동(경계 부분 주의) 
#문제 조건 오해(23:59 까지 끝나는게 아니라 최대 시작 시간이 23:59)
#예정: 시간 관련 문제 -> 일일이 초단위 진행하지말고 사건 사이의 시간 차 이용한 풀이 

def convert(time):
    h,m = map(int,time.split(':'))
    return h*60 + m

def solution(plans):
    plans = [ [plan[0],convert(plan[1]),int(plan[2])] for plan in plans]
    plans.sort(key=lambda x: x[1])
    
    progress = {i:0 for i in range(len(plans))}
    doing,pending = -1,[]
    ended = []
    
    now_time = 0
    while len(ended)!=len(plans):
        for i,plan in enumerate(plans):
            if now_time == plan[1]:
                pending.append(doing)
                doing = i
                
        if doing == -1:
            now_time+=1
            continue
            
        progress[doing]+=1
        if progress[doing] == plans[doing][2]:
            ended.append(doing)
            doing = pending.pop()
        
        now_time+=1
        
    
    return [plans[idx][0] for idx in ended]
    
        
        
    