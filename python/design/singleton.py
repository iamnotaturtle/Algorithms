class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance != None:
            raise Exception('This is a singleton!')
        else:
            Singleton._instance = self

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance
    
s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)
