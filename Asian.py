import Restaurant1

class AsianBuilder(Builder):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self._restaurant = Restaurant1()
        
     #getters to return the restaurant object back
    @property 
    def getRestaurant(self) -> restaurant:
        restaurant = self._restaurant
        self.reset()
        return restaurant
    
    def getLocation(self):
        return self.location
    
    def getMenuItems(self):
        return self.menuItem
  

    def setRestaurant(self, name) -> None:
        self._restaurant.addName(name)

    def setLocation(self, location) -> None:
        self._restaurant.addLocation(location)

    def setMenuItem(self, item, price) -> None:
        self._restaurant.addMenuItem(item, price)

    
