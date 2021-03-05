import json


def getTrie(words):
    if not words:
        return {}
    
    root = {}
    for word in words:
        cur = root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = {}
    return root

def getWords(chars, root):
    if not chars or not root:
        return []
    
    n = len(chars)
    res = []
    for i in range(n):
        if chars[i] in root:
            res.append(getWord(chars, set([i]), root[chars[i]], chars[i]))

    return res
def getWord(chars, visited, node, word):
    if '#' in node:
        return word
    
    for i in range(len(chars)):
        if i not in visited and chars[i] in node:
            visited.add(chars[i])
            node = node[chars[i]]
            word += chars[i]
            return getWord(chars, visited, node, word)

words = ['use', 'aloe', 'now', 'zoo']
chars = ['o', 'o', 'e', 's', 'u', 'z']
root = getTrie(words)
assert(getWords(chars, root) == ['use', 'zoo'])
