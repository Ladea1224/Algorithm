"""
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
"""
#리팩토링: 1 개수만 세면 된다. 굳이 이진수 문자열을 만들 필요 없다.
def solution(n):
    def count_ones(number):
        count = 0
        while number:
            count += number % 2
            number //= 2
        return count

    target = count_ones(n)

    i = n + 1
    while count_ones(i) != target:
        i += 1

    return i