# Add without using + oprator
def add(a, b):
    if b == 0:
        return a

    sm = a ^ b
    carry = (a & b) << 1

    return add(sm, carry)


assert(add(234, 789) == 1023)

def addIterative(a, b):
    while b != 0:
        a, b = a ^ b, (a & b) << 1
    
    return a

assert(addIterative(234, 789) == 1023)