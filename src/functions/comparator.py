def count_distance(e, village):
    ex = e[0:3]
    ey = e[4:7]
    vx = village[0:3]
    vy = village[4:7]
    dx = abs(float(ex) - float(vx))
    dy = abs(float(ey) - float(vy))
    return int(dx) if dx > dy else int(dy)