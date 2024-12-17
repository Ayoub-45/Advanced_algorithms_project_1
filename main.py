from MenuManagement import MenuManagement
dishes={}
menu_management=MenuManagement(dishes)
menu_management.add("pizza",12)
menu_management.add("Burger",18)
menu_management.remove("pizza")
menu_management.display()
