from __future__ import annotations
import Restaurant
import Builder


class AsianBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._restaurant = Restaurant()
        self.location = ""
        self.menuItem = {}

    # getters to return the restaurant object back
    @property
    def getRestaurant(self) -> Restaurant:
        self.reset()
        return self._restaurant

    def getLocation(self):
        return self.location

    def getMenu(self):
        return self.menuItem

    def setRestaurant(self, name) -> None:
        self._restaurant.addName(name)

    def setLocation(self, location) -> None:
        self._restaurant.addLocation(location)

    def setMenu(self, item, price) -> None:
        self._restaurant.addMenuItem(item, price)
