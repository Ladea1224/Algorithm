directions = [(0,1),(0,-1),(-1,0),(1,0)]
def solution(board, h, w):
    
    color = board[h][w]
    cnt = 0
    for dh,dw in directions:
        nh = h+dh
        nw = w+dw
        if not( 0<=nh<len(board) and 0<=nw<len(board[0]) ) : continue
        if board[nh][nw] == color:
            cnt+=1
    
    return cnt
        