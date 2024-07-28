def asteroid_collision(asts, start=0):
    if start > len(asts) - 1:
        return asts
    if start and asts[start - 1] > 0 and asts[start] < 0:
        left = abs(asts[start - 1])
        right = abs(asts[start])
        if left < right:
            asts.pop(start-1)
            return asteroid_collision(asts, start-1)
        elif left > right:
            asts.pop(start)
            return asteroid_collision(asts, start)
        else:
            asts.pop(start)
            asts.pop(start-1)
        return asteroid_collision(asts, start-1)
    return asteroid_collision(asts, start+1)

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))