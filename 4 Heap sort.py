# we need to have heapify sort. Which create and recreate array/list into a tree
# left leaf, right leaf
def Heapify(A, n, i):
    l = i*2 + 1
    r = i*2 + 2
    key = i
    if l < n and A[key] < A[l]:
        key = l
    if r < n and A[key] < A[r]:
        key = r
    if key != i:
        A[key], A[i] = A[i], A[key]
        Heapify(A, n, key)

def Heap_sort(A):
    n = len(A)
    for i in range((int(n/2) - 1), -1, -1):
        Heapify(A, n, i)
    for i in range( n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        Heapify(A, i, 0)


A = [4, 3, 1, 5, 10, 2]
Heap_sort(A)
print(A)

