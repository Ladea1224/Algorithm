import math
def solution(r1, r2):
    answer = 0
    for x in range(1,r2+1):
        l = max(0,r1*r1 - x*x)
        r = r2*r2 - x*x
        min_y,max_y = math.ceil(math.sqrt(l)),math.floor(math.sqrt(r))
        answer += max_y - min_y + 1
        
    answer*=4
    return answer