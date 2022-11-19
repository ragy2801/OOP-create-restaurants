from Builder import Builder
from Restaurant import Restaurant


class AsianBuilder(Builder):
    def __init__(self) -> None:
        super().__init__()

    # getters to return the restaurant object back
    def getRestaurant(self):
        return self._restaurant.name

    def getLocation(self):
        return self._restaurant.location

    def getMenu(self):
        return self._restaurant.menu

    def setLocation(self, location) -> None:
        self._restaurant.addLocation(location)

    def setMenuItem(self, menu) -> None:
        self._restaurant.addMenuItem(menu)

    def setRestaurant(self, name) -> None:
        self._restaurant.addName(name)
