def insertion(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

# test
A = [2, 3, 1, 2, 5, 9]
insertion(A)
print(A)


