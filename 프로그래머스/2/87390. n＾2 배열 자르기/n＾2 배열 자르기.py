# 행 번호 = row = idx/n  (0부터 시작 기준)
# row 에서 원소: row+1 이 row+1개 나오고, 이후 1씩 커짐
# 예를들어 row=2 이면 3,3,3,4/ row=5 이면 6,6,6,6,6,6,7,8,...
# 따라서 idx-n*row <= row 인 경우 값 = row+1, 아니면 값 = row+1 + (idx-n*row-row)

def solution(n, left, right):
    answer = []
    for idx in range(left,right+1):
        row = idx//n
        if idx-n*row<=row:
            answer.append(row+1)
        else:
            answer.append(row+1 + (idx-n*row-row))

    return answer
    
    