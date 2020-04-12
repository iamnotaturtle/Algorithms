from collections import deque

graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anju', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'thom': [],
    'anju': [],
    'peggy': [],
    'jonny': [],
}

def person_is_seller(name):
    return name[-1] == 'm'

# BFS O(|V| + |E|)
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("mango seller", person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

search('you')