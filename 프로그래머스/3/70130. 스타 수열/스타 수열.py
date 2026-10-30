from collections import Counter

def solution(a):
    cnts = Counter()
    last = Counter()
    
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            continue
        
        for x in (a[i],a[i+1]):
            if i<last[x]: continue
            cnts[x] += 1
            last[x] = i+2
        
    return max(cnts.values(),default=0)*2
    