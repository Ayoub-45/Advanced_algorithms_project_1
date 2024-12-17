class MenuManagement:
    def __init__(self,dishes:{}):
        self.dishes=dishes
    def add(self,name,price):
        self.dishes[name]=price
        self.display()
    def remove(self,name):
            if name in self.dishes:
                while True:
                    yes_or_no = input(f"Are you sure you want to delete {name}? [y/n]: ").lower()
                    if yes_or_no == "y":
                        del self.dishes[name]
                        print(f"{name} has been removed from the menu!")
                        break
                    elif yes_or_no == "n":
                        print("No changes were made.")
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
            else:
                print(f"{name} does not exist in the menu.")
    def modify(self,)
    def display(self):
        print("####Menu#####")
        print(self.dishes)
        print("#############")         