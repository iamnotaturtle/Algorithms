# Returns permutations of characters
def permute(s, length):
    if length == 1:
        return s
    
    return [
        x + y
        for x in permute(s, 1)
        for y in permute(s, length - 1)
    ]

print(permute(['a', 'b', 'c'], 3))
