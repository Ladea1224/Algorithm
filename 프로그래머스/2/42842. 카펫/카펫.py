# (n+m-2)*2 = brown ,  3<=n
# n*m-brown= yellow
# brown 범위 따라 시간복잡도 대략 10^3 * 10^3 
# 가로=n=i, 세로=m=j
def solution(brown, yellow):    
    for i in range(3,2000):
        for j in range(i,2000):
            b = (i+j-2)*2 
            y = i*j-b
            if (b,y) == (brown,yellow):
                return [j,i]
    
