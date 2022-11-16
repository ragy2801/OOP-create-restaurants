from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class RestaurantBuilder(ABC):
    
    @property
    @abstractmethod
    def setRestaurant(self, name) -> None:
        pass
    
    @abstractmethod
    def setLocation(self, location) -> None:
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
    def getMenu() -> None:
        pass
