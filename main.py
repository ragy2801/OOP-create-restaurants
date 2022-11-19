from Request import Request
from AsianBuilder import AsianBuilder
from MexicanBuilder import MexicanBuilder
from ItalianBuilder import ItalianBuilder


def createRestaurant(request, buildRestaurant, name, location):
    builder = buildRestaurant
    request.setbuilder(builder)

    menu = createMenu()
    request.addRequest(name, location, menu)


def createMenu():
    menu = {}

    while True:
        menuItem = input("Enter menu item and price seperated by space or QUIT: ")
        if menuItem == "QUIT":
            break
        else:
            item, price = menuItem.split(" ")
            menu[item] = price
    return menu


if __name__ == '__main__':
    request = Request()

    while True:
        userInput = input("Press (1) Add a restaurant \n"
                          "Press (2) to view a restaurant \n"
                          "Press (3) to quit \nEnter input: ")
        if userInput == "3":
            break

        if userInput == "1":
            typeOfrest = input("Type of Restaurants available \n"
                               "Asian, Mexican, Italian: ")
            name = input("Name for the resaurant: ")
            location = input("What is the location for the restaurant: ")

            if typeOfrest.startswith("A"):
                builder = AsianBuilder()
                createRestaurant(request, builder, name, location)
            elif typeOfrest.startswith("M"):
                builder = MexicanBuilder()
                createRestaurant(request, builder, name, location)
            elif typeOfrest.startswith("I"):
                builder = ItalianBuilder()
                createRestaurant(request, builder, name, location)

        if userInput == "2":
            request.viewRestaurant()


