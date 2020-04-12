# Pattern with ability to restore object to previous state
# Consists of memento, originator and caretaker

# Contains state and returns state
class Memento():
    def __init__(self, state):
        self._state = state

    def getSavedState(self):
        return self._state

# Contains memento object
class Originator():
    def __init__(self, state):
        print('Originator, init state:', state)
        self._state = state
    
    def saveToMemento(self) -> Memento:
        print('Originator, saving to memento:', self._state)
        return Memento(self._state)
    
    def restoreFromMemento(self, memento: Memento):
        self._state = memento.getSavedState()
        print('Originator, restoring from memento:', self._state)

# Caretaker
# Does something to Originator, but wants to save state
# Asks for memento object first
savedStates = []
originator = Originator('state1')
savedStates.append(originator.saveToMemento())
originator = Originator('state2')
savedStates.append(originator.saveToMemento())

originator.restoreFromMemento(savedStates[0])