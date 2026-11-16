#1개 단위~ len(s)개 단위,  시간: 10^3 * 10^3 

# s[:k] == s[k:2k], s[k:2k] == s[2k:3k],   ...

def solution(s):
    def getLen(k):  #k개 단위로 잘랐을 때의 길이
        result = ""
        idx = 0
        
        while idx<len(s):
            n = 1
            while s[idx+ k*(n-1):idx+ k*n]==s[idx+ k*n:idx+ k*(n+1)]:
                n+=1

            if n!=1:
                result += str(n)
            result += s[idx+ k*(n-1):idx+ k*n]
            idx += n*k
        return len(result)
    
    answer = 1e9
    for i in range(1,len(s)+1):
        answer = min(answer,getLen(i))
        
    return answer