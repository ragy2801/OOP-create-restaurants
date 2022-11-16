

class AsianBuilder(Builder):
    def __init__(self) -> None:
        

    def setRestaurant(self, name):
        self.name = name

    def getRestaurant(self):
        return self.name

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setMenuItem(self, menuItem):
        self.menuItem.append(menuItem)

    def getMenuItems(self):
        return self.menuItem

    def setItemPrice(self, price):
        self.price.append(price)

    def getItemPrice(self):
        return self.price
