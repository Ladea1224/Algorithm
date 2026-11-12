# 1.시간복잡도?? (최대 길이 10이 아니라 7 주의)

# 2.가지치기 필요??

# 3.소수판별 에라토스테네스 체? 
#   만약 쓴다면 최대 공간 7654321니까 대충 4*10^7 = 40MB, 
#   파이썬 기준 몇 배 더해야 하니까 메모리 초과...

# 4. permutation 라이브러리 쓴다면? (더 복잡한가?)

# 5. 역순까지 전부 고려하므로 선택한거 이후부터 순회하는 방식 아님 주의..

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    add = []
    vis = [0]*len(numbers)
    primes = set()
    
    def dfs():
        nonlocal answer
        if add and isPrime():
            answer+=1
        
        for i in range(len(numbers)):
            if vis[i]: continue
            
            add.append(numbers[i])
            vis[i] = 1
            
            dfs()
            
            vis[i] = 0
            add.pop()
            
    def isPrime():
        n = int("".join(add))
        if n<2: return False
        
        for i in range(2,n):
            if i*i>n: break
            if n%i==0: return False
        
        if n in primes: return False
        primes.add(n)
        return True
    
    dfs()
    return answer