class Strategy:
    def __init__(self, func = None):
        if func:
            self.execute = func

    def execute(self):
        print("Original execution")

def executeReplacement1():
    print("Strategy 1")

def executeReplacement2():
    print("Strategy 2")

strategy = Strategy()
strategy1 = Strategy(executeReplacement1)
strategy2 = Strategy(executeReplacement2)

strategy.execute()
strategy1.execute()
strategy2.execute()
