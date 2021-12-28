def SriFactorial(n):
    factorial = 1;
    if (n == 0):
        return factorial
    else:
        for ii in range(n):
            factorial*=(ii+1)
        # print(ii+1)

    return (factorial)
