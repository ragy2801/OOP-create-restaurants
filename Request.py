from __future__ import annotations
import Builder


class Request:
    def __init__(self):
        self._builder = None

    def builder(self) -> Builder:
        return self._builder

    def setbuilder(self, builder: Builder) -> None:
        self._builder = builder

    # request types
    def addRequest(self, name, location, menu) -> None:
        self._builder.setRestaurant(name)
        self._builder.setLocation(location)
        self._builder.setMenuItem(menu)

    def viewRequest(self) -> None:
        print(self._builder.getRestaurant())
        print(self._builder.getLocation())
        print(self._builder.getMenu())
