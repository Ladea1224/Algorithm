#반복문 내부에서의 순서 배치 혼동(경계 부분 주의) 
#문제 조건 오해(23:59 까지 끝나는게 아니라 최대 시작 시간이 23:59)
"""
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
"""
#시간 관련 문제 -> 일일이 초단위 진행하지말고 사건 사이의 시간 차 이용한 풀이 
#현재-과거 방식: 과거 저장 필요, 루프 전체 순회 가능
#현재-미래 방식: 과거 저장 필요 X, 마지막 부분 루프 불가능, 예외처리 필요
#보통 전자가 직관적인 느낌...

def convert(time):
    h,m = map(int,time.split(':'))
    return h*60 + m

def solution(plans):
    plans = [ [plan[0],convert(plan[1]),int(plan[2])] for plan in plans]
    plans.sort(key=lambda x: x[1])
    
    stack,answer=[],[]
    prev = 0
    for name,start,time in plans:
        diff = start-prev
        while stack and diff>0: #과거 처리 - stack 에 작업 있을 때, diff 갉아먹음
            if stack[-1][1]<=diff:
                diff -= stack[-1][1]
                answer.append(stack[-1][0])
                stack.pop()
            else:
                stack[-1][1] -= diff
                diff = 0
        stack.append([name,time]) #현재 처리 - 스택에 작업 추가 
        prev = start
        
    while stack:
        answer.append(stack.pop()[0])
        
    return answer
        
    