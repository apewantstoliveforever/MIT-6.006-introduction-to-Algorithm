def Merge(A):
    n = len(A)
    if n > 1:
        mid = int(n/2)
        L = A[:mid]
        R = A[mid:]
        Merge(L)
        Merge(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                k += 1
                i += 1
            else:
                A[k] = R[j]
                k += 1
                i += 1
        while i < len(L):
            A[k] = L[i]
            k += 1
            i += 1
        while j < len(R):
            A[k] = R[j]
            k += 1
            j += 1


A = [1, 3, 5, 7, 8]
Merge(A)
print(A)