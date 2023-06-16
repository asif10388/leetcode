def find_sum(n):
    if n == 1:
        return 1
    else:
        return n + find_sum(n - 1)


print(find_sum(5))
