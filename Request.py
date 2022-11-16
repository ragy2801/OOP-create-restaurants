from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Request:
    def __init__(self):
        self._restaurant = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder
        
    # request types
    def addrequest(self, name, location) -> None:
#         self._restaurant.setRestaurant(name)
#         self._restaurant.setLocation(location)

    def viewRequest(self, restaurant: Restaurant) -> None:
#         restaurant.getRestaurant()
#         restaurant.getLocation()
#         restaurant.getMenuItem()
