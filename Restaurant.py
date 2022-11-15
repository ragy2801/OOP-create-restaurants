from abc import ABC, abstractmethod


class Restaurant(ABC):

    @abstractmethod
    def setRestaurant(self, name):
        pass

    def getRestaurant(self):
        pass

    def setLocation(self, location):
        pass

    def getLocation(self):
        pass
