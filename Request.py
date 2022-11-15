import Restaurant


class Request:
    def __init__(self, restaurant: Restaurant):
        self._restaurant = restaurant

    def restaurant(self) -> Restaurant:
        return self._restaurant

    def setRestaurant(self, restaurant: Restaurant):
        self._restaurant = restaurant

    # request types
    def addrequest(self, name, location) -> None:
        self._restaurant.setRestaurant(name)
        self._restaurant.setLocation(location)

    def viewRequest(self, restaurant: Restaurant) -> None:
        restaurant.getRestaurant()
        restaurant.getLocation()
        restaurant.getMenuItem()
