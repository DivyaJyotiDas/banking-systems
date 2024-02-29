from abc import ABC, abstractmethod

class Repo(ABC):
    
    @abstractmethod
    def create(self):
        raise NotImplemented
    
    @abstractmethod
    def update(self):
        raise NotImplemented
    
    @abstractmethod
    def list(self):
        raise NotImplemented
    
    @abstractmethod
    def delete(self):
        raise NotImplemented