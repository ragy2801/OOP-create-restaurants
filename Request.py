from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Request:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder
        
    # request types
    def addrequest(self, name, location, item, price) -> None:
        self._builder.setRestaurant(name)
        self._builder.setLocation(location)
        self._builder.setMenu(item, price)

    def viewRequest(self, restaurant: Restaurant) -> None:
        self._builder.getRestaurant()
        self._builder.getLocation()
        self._builder.getMenuItem()
