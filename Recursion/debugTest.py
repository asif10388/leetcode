# def fnThree():
#     print("Three")


# def fnTwo():
#     fnThree()
#     print("Two")


# def fnOne():
#     fnTwo()
#     print("One")


# fnOne()

def rec4(n):
    if n <= 4:
        return

    rec4(n-1)
    print(n)
    rec4(n-2)


rec4(8)
