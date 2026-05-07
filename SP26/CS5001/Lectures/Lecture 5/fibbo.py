def calculatehanoi(n):
    if n==0
        return 0
    elif n==1:
        return 1
    else:
        result = calculatehanoi(n-1)*2+1
    return result

    n = int("How many rings do we have?")
