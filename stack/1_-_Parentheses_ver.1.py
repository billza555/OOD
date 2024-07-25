def checkParenthese(parenthese):
    parentheses = []
    miss = 0
    for parent in parenthese:
        if parent in ":":
            if parentheses and parentheses[-1] in ":":
                parentheses.pop()
            else:
                parentheses.append(parent)
        if parent in "([":
            parentheses.append(parent)
        elif parent in ")":
            if parentheses and parentheses[-1] in "(":
                parentheses.pop()
            else:
                miss += 1
        elif parent in "]":
            if parentheses and parentheses[-1] in "[":
                parentheses.pop()
            else:
                miss += 1
    miss += len(parentheses)
    return miss

parentheses = list(input("Enter Input : "))
missValue = checkParenthese(parentheses)
print(missValue)
if not missValue:
    print("Perfect ! ! !")