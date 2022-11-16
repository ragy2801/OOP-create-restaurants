

class AsianBuilder(Builder):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self._restaurant = Restaurant()
        
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
  

    def setRestaurant(self) -> None:
        self._restaurant.addName(#parameterlist)

    def setLocation(self):
        self._restaurant.addLocation(#parameterlist)

    def setMenuItem(self, menuItem):
        self._restaurant.addMenuItem(#parameter)

    
