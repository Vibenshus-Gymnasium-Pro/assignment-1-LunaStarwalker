def sale():
    n, x = map(int, input().split())
    items = list(map(int, input().split()))[:n]

    items.sort()

    print(items)

    for item in items:
        if item >= x:
            items.remove(item)

    if n == 1 or len(items) == 1:
        print("1")
    elif items[-1] + items[-2] <= x:
        print(n)
    else:
        for i, c in enumerate(items):
            if c + items[i+1] > x:
                print(i+1)
                break


if __name__ == "__main__":
    sale()











