"""
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
"""

#리팩토링: 매번 이동 할 필요 X(기준 block 따로 빼기), 문자열 만들 필요 X(길이만 저장)
def solution(s):
    def getLen(k):
        length = 0
        idx = 0

        while idx < len(s):
            block = s[idx:idx + k]
            count = 1

            while block == s[idx + k*count:idx + k*(count + 1)]:
                count += 1

            length += len(block)
            if count > 1:
                length += len(str(count))

            idx += count * k

        return length

    answer = len(s)
    for k in range(1, len(s) // 2 + 1):
        answer = min(answer, getLen(k))

    return answer