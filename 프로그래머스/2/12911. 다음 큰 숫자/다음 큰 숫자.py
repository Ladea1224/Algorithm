def solution(n):
    def getBi(n):
        result = ""
        while n:
            result = str(n%2) + result
            n=n//2
        return result
        
    nBi = getBi(n)
    nCnt = nBi.count("1")
    
    i = n+1
    while True:
        bi = getBi(i)
        if bi.count("1")==nCnt:
            return i
        i+=1
    
