#시간복잡도 10! 인가? 10^10인가..?/ 0으로 시작하는거나 홀짝으로 가지치기 해줘야하나?
#소수판별까지 생각하면 시간 초과 아닌가? 에라토스테네스의 체 필요한가?
# dfs 말고 permutation 라이브러리 쓸걸 그랬나?
# 71같은 역순도 돼야하니까 선택 다음부터 시작이 아니라 선택 부분 pass 하는 식으로 해야겠다

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