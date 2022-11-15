import Request
import Asian
import Restaurant

# https://refactoring.guru/design-patterns/strategy/python/example
if __name__ == '__main__':

    while True:
        userInput = input("Press (1) Add a restaurant \n"
                          "Press (2) to view a restaurant \n"
                          "Press (3) to quit: ")
        if userInput == 3:
            break

        name = input("Name for the resaurant: ")

        if userInput == 1:
            typeOfrest = input("Type of Restaurants available \n"
                               "Asian, Mexican, Italian: ")
            location = input("What is the location for the restaurant: ")

            # TODO: make function to determine type of restaurant
            if typeOfrest.startswith("A"):
                request = Request(Asian())
                request.addrequest(name, location)


            # TODO: make function to add menu items
            while True:
                itemInfo = input("Enter menu item name and price separate by space: ")
                item, price = itemInfo.split(" ")
                # asian.setMenuItem(item)
                # asian.setItemPrice(price)
