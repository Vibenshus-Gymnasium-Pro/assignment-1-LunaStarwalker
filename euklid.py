def euklid(A, B):
    if B != 0:
        r = A % B
        euklid(B, r)

    elif B == 0:
        print(A)

euklid(7020,4960)
print(7020/20)
print(4960/20)