def SriStdVar(x):

    import math

    n = len(x)

    meanval = sum(x)/n

    y = [i**2 for i in x]   #looks like vectorisation - this is called list comprehension

    return y                #Identation matters!!
    # return [y]            #A list of lists is possible!
