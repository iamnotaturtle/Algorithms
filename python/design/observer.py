# Consists of Observer and Observable
# Observable notifies observer when it changes state
class Observer:
    def __init__(self, observable: 'Observable'):
        observable.registerObserver(self)

    def notify(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)

class Observable:
    def __init__(self):
        self._observers = []
    
    def registerObserver(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

subject = Observable()
observer = Observer(subject)
subject.notify('test')