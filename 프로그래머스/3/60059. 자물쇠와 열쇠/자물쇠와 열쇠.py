def solution(key, lock):
    m, n = len(key), len(lock)

    def rotate(key):
        result = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                result[m - 1 - j][i] = key[i][j]

        return result

    def possible(dr, dc):
        board = [row[:] for row in lock]

        for r in range(m):
            for c in range(m):
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue

                board[nr][nc] += key[r][c]

        return all(x == 1 for row in board for x in row)

    # 열쇠를 완전히 밖에 두면 열리는 경우
    if all(x == 1 for row in lock for x in row):
        return True

    for _ in range(4):
        for dr in range(-m + 1, n):
            for dc in range(-m + 1, n):
                if possible(dr, dc):
                    return True

        key = rotate(key)

    return False