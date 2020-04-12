import itertools

class State:
    def __init__(self):
        self.stations = itertools.cycle()
        self.name = None

    def scan(self):
        print("Scanning... Station is", next(self.stations), self.name)

class AmState(State):
    def __init__(self, radio):
        self.name = "AM"
        self.radio = radio
        self.stations = itertools.cycle(["1010", "1250", "1380", "1510"])
    
    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        self.name = "FM"
        self.radio = radio
        self.stations = itertools.cycle(["92.3", "100.3", "103.5", "97.1"])
    
    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate

class Radio:
    def __init__(self):
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate
    
    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

radio = Radio()
actions = ([radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2) * 2
for action in actions:
    action()