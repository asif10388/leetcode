# def matrixProduct(m1, m2):
#     c11 = (m1[0][0] * m2[0][0]) + (m1[0][1] * m2[1][0])
#     c12 = (m1[0][0] * m2[0][1]) + (m1[0][1] * m2[1][1])
#     c21 = (m1[1][0] * m2[0][0]) + (m1[1][1] * m2[1][0])
#     c22 = (m1[1][0] * m2[0][1]) + (m1[1][1] * m2[1][1])

#     product = [[c11, c12], [c21, c22]]

#     return product


# print(matrixProduct([[2, 3], [4, 5]], [[5, 6, ], [7, 8]]))

_ = None
A = [0] * 4
B = [0] * 4

print(A)

for i in range(0, 2):
    if _ == None:
        _ = list(input())
        print(A[i + i + 0])
    A[i+i+0] = int(_.pop(0))
    A[i+i+1] = int(_.pop(0))

    print(_)

    _ = None

# for i in range(0, 2):
#     if _ == None:
#         _ = input().split()
#     B[i+i+0] = int(_.pop(0))
#     B[i+i+1] = int(_.pop(0))
#     _ = None