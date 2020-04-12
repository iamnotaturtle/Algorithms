from abc import ABC, abstractmethod
from typing import AnyStr

class A(ABC):
    @abstractmethod
    def whois(self) -> AnyStr:
        pass

class Concrete(A):
    def whois(self) -> AnyStr:
        return f"Concrete: {self}"

c = Concrete()
print(c.whois())