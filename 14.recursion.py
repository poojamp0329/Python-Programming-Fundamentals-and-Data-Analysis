#recursion 

def tri_recursion(k):
    if (k>0):
        result = k+ tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result

tri_recursion(6)

def factorial(k):
    if (k>1):
        result= k* factorial(k-1)
        print(result)
    else:
        result = 1
    return result
factorial(5)
