
def quickSort(A, start, end):
    if start < end:
        q = pivot(A, start, end)
        quickSort(A, start, q-1)
        quickSort(A, q+1, end)


def pivot(A, start, end):
    #choosing pivot element
    piv = A[end]
    i = start - 1

    for j in range(start, end):
        if A[j] <= piv:
            i += 1
            A[j], A[i] = A[i], A[j]

    A[i+1], A[end] = A[end], A[i+1]
    return i+1


myArr = [1, 0, 5, 8, 3, 5]
quickSort(myArr, 0, 5)
print(myArr)