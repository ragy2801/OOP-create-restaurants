from typing import Any


class Restaurant:
    def __init__(self) -> None:
        self.name = ""
        self.location = ""
        self.menu = {}

    def addName(self, name: Any) -> None:
        self.name = name

    def addLocation(self, location: Any) -> None:
        self.location = location

    def addMenuItem(self, menu) -> None:
        self.menu = menu

    def menuList(self) -> None:
        print(self.menu)
