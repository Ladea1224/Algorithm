def convert(s):
    a,b,c = map(int,s.split("."))
    return a*12*28 + b*28 + c
    
def solution(today, terms, privacies):
    termDay = {}
    for term in terms:
        type,dur = term.split()
        termDay[type] = int(dur)*28
        
    answer = []
    today = convert(today)
    for i,priv in enumerate(privacies):
        start,type = priv.split()
        endDay = convert(start) + termDay[type]
        if(today >= endDay):
            answer.append(i+1)
        
    return answer