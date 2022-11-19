from Request import Request
from AsianBuilder import AsianBuilder


def createRestaurant(buildRestaurant, name, location):
    request = Request()
    builder = buildRestaurant
    request.setbuilder(builder)

    menu = createMenu()
    request.addRequest(name, location, menu)


def createMenu():
    menu = {}

    while True:
        item, price = input("Enter menu item and price seperated by space or QUIT: ").split(" ")
        menu[item] = price
        if item or price == "QUIT":
            break
    return menu


if __name__ == '__main__':

    while True:
        userInput = input("Press (1) Add a restaurant \n"
                          "Press (2) to view a restaurant \n"
                          "Press (3) to quit \nEnter input: ")
        if userInput == "3":
            break

        name = input("Name for the resaurant: ")

        if userInput == "1":
            typeOfrest = input("Type of Restaurants available \n"
                               "Asian, Mexican, Italian: ")
            location = input("What is the location for the restaurant: ")

            if typeOfrest.startswith("A"):
                builder = AsianBuilder()
                createRestaurant(builder, name, location)

