def water_jug(x, y, target):
    a, b = 0, 0
    while (a != target and b != target):
        if a == 0:           # fill jug X
            a = x
            print(a, b)
        elif b == y:         # empty jug Y
            b = 0
            print(a, b)
        else:                # pour X -> Y
            pour = min(a, y - b)
            a -= pour
            b += pour
            print(a, b)
    print("Target achieved:", a, b)

water_jug(4, 3, 2)
