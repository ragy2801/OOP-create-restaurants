from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def setRestaurant(self) -> None:
        pass

    @abstractmethod
    def setLocation(self) -> None:
        pass

    @abstractmethod
    def setMenuItem(self) -> None:
        pass

    @abstractmethod
    def getRestaurant(self) -> None:
        pass

    @abstractmethod
    def getLocation(self) -> None:
        pass

    @abstractmethod
    def setMenu(self) -> None:
        pass

    @abstractmethod
    def getMenu(self) -> None:
        pass
