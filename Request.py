from __future__ import annotations
import Builder


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
    def addRequest(self, name, location, item, price) -> None:
        self._builder.setRestaurant(name)
        self._builder.setLocation(location)
        self._builder.setMenu(item, price)

    def viewRequest(self, restaurant: object) -> None:
        self._builder.getRestaurant(restaurant)
        self._builder.getLocation(restaurant)
        self._builder.getMenuItem(restaurant)
