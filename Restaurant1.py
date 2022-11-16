class Restaurant():
  def __init__(self) -> None:
    self.name = ""
    self.location = ""
    self.menu = {}
    
  def addName(self, name: Any) -> None:
     self.name = name
      
  def addLocation(self, location: Any) -> None:
      self.location = location
  
  def addMenuItem(self, itemName: Any, itemPrice: Any) -> None:
      self.menu[itemName] = itemPrice
  
  def menuList(self) -> None:
      print(menu)
               
