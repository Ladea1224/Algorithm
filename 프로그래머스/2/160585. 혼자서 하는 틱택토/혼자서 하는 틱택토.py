"""
최초 실패 코드
1.세는 방식 난잡함
2.조건 제대로 나누지 못함

def solution(board):
    #전체 개수
    cntO = sum(1 for row in board for x in row if x=="O")
    cntX = sum(1 for row in board for x in row if x=="X")
    
    lineO,lineX = 0,0
    #행
    lineO += sum(1 for row in board if all(x=="O" for x in row))
    lineX += sum(1 for row in board if all(x=="O" for x in row))
    #열
    lineO += sum(1 for row in zip(*board[::-1]) if all(x=="O" for x in row))
    lineX += sum(1 for row in zip(*board[::-1]) if all(x=="X" for x in row))
    #대각1
    lineO += all(board[i][i]=="O" for i in range(3)) 
    lineX += all(board[i][i]=="X" for i in range(3))
    #대각2
    lineO += all(list(zip(*board[::-1]))[i][i]=="O" for i in range(3)) 
    lineX += all(list(zip(*board[::-1]))[i][i]=="X" for i in range(3))
    
    if lineO==lineX==0:
        return 1 if cntO==cntX or cntO==cntX+1 else 0
    elif lineX and lineO:
        return 0
    elif lineX>=2:
        return 0
    elif lineX==1:
        return 1 if cntO==cntX else 0
    elif lineO>=3:
        return 0
    elif lineO==2:
        return 1 if cntO==5 and cntX==4 else 0
    elif lineO==1:
        return 1 if cntO==cntX+1 else 0
"""    

# 리팩토링
# 3x3 상황이라 특수하게 가능한 구현 상황.. (턴 조건 체크만 해도 승리 조건 일부 걸러지는 등)

def win(board,player):
    # 가로
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
            
    # 세로
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
            
    # 대각선
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
        
    return False


def solution(board):
    #전체 개수
    cntO = sum(row.count("O") for row in board)
    cntX = sum(row.count("X") for row in board)
    
    #승리 여부
    winO = win(board,"O")
    winX = win(board,"X")
    
    #턴 조건 위반
    if not (cntO==cntX or cntO==cntX+1): return 0

    #승리 후 중단 조건 위반(중단 조건 위반 중 한 player가 2번 이기는 상황은 턴 조건에서 걸러짐)
    if winO and winX: return 0

    #승리 case에 따라 턴 조건 위반 여부 상세 확인
    if winO and cntO != cntX+1: return 0
    if winX and cntO != cntX: return 0 
    
    return 1
    
    
    
    
    
    
    
    
    
    