def bi_search(l, r, arr, x):
    if l > r:
        return False
    medium = (l + r) // 2
    if x < arr[medium]:
        return bi_search(l, medium-1, arr, x)
    elif x > arr[medium]:
        return bi_search(medium+1, r, arr, x)
    else:
        return True

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))