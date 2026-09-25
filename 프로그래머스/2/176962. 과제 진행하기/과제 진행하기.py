#전부 분 단위로 바꾸어 생각

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
        if doing != -1 and progress[doing] == plans[doing][2]:
            ended.append(doing)
            doing = pending.pop()
            
        for i,plan in enumerate(plans):
            if now_time == plan[1]:
                pending.append(doing)
                doing = i
                
        if doing == -1:
            now_time+=1
            continue
    
        progress[doing]+=1
        now_time+=1
        
    
    return [plans[idx][0] for idx in ended]
    
        
        
    