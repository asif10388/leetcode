def paintingX(N, R, C):
    row = []
    grid = ""

    dX1, dY1 = R, C
    dX2, dY2 = R, C
    dX3, dY3 = R, C
    dX4, dY4 = R, C

    # Creating the grid
    for i in range(N):
        row.append(["."] * N)

    while (True):
        if 0 <= dX1 <= N and 0 <= dY1 <= N:
            row[dX1 - 1][dY1 - 1] = "*"

        if (dX1 - 1) > 0 and (dY1 - 1) > 0:
            dX1 -= 1
            dY1 -= 1
        else:
            break

    while (True):
        if 0 <= dX2 <= N and 0 <= dY2 <= N:
            row[dX2 - 1][dY2 - 1] = "*"

        if (dX2 - 1) < (N-1) and (dY2 - 1) > 0:
            dX2 += 1
            dY2 -= 1
        else:
            break

    while (True):
        if 0 <= dX3 <= N and 0 <= dY3 <= N:
            row[dX3 - 1][dY3 - 1] = "*"

        if (dX3 - 1) > 0 and (dY3 - 1) < (N-1):
            dX3 -= 1
            dY3 += 1
        else:
            break

    while (True):
        if 0 <= dX4 <= N and 0 <= dY4 <= N:
            row[dX4 - 1][dY4 - 1] = "*"

        if (dX4 - 1) < (N - 1) and (dY4 - 1) < (N-1):
            dX4 += 1
            dY4 += 1
        else:
            break

    # Printing the grid
    for j in range(N):
        grid += " ".join(row[j]) + "\n"

    print(grid)


print(paintingX(11, 6, 6))
print(paintingX(7, 3, 7))
