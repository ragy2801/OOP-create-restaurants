from __future__ import annotations
from abc import ABC, abstractmethod
from Restaurant import Restaurant


class Builder(ABC):
    def __init__(self) -> None:
        self._restaurant = Restaurant()
        self.location = ""
        self.menuItem = {}

    @abstractmethod
    def setLocation(self, location) -> None:
        pass

    @abstractmethod
    def setMenuItem(self, menu) -> None:
        pass

    @abstractmethod
    def getRestaurant(self) -> None:
        pass

    @abstractmethod
    def getLocation(self) -> None:
        pass

    @abstractmethod
    def getMenu(self) -> None:
        pass

    @abstractmethod
    def setRestaurant(self, name) -> None:
        pass
