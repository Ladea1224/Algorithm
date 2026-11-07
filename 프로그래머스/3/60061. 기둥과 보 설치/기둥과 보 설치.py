
GI, BO = 0, 1

def solution(n, build_frame):
    things = set()

    def can_gi(x, y):
        if y == 0: return True
        if (x, y, BO) in things: return True
        if (x-1, y, BO) in things: return True
        if (x, y-1, GI) in things: return True
        return False

    def can_bo(x, y):
        if (x, y-1, GI) in things: return True
        if (x+1, y-1, GI) in things: return True
        if (x-1, y, BO) in things and (x+1, y, BO) in things:
            return True
        return False

    def is_valid():
        for x, y, a in things:
            if a == GI:
                if not can_gi(x, y): return False
            elif a == BO:
                if not can_bo(x, y): return False
        return True

    for x, y, a, b in build_frame:
        if b == 0:
            things.remove((x, y, a))

            if not is_valid():
                things.add((x, y, a))

        else:
            things.add((x, y, a))

            if not is_valid():
                things.remove((x, y, a))

    return sorted(list(things))
