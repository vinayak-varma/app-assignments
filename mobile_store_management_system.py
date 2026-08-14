class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def categorize(self):
        if self.price>=50000:
            return "Premium"
        elif self.price>=20000:
            return "Mid-range"
        else:
            return "Budget"
    def display(self):
        print(f"{self.brand}\t\t{self.model}\t\t{self.price}\t\t{self.categorize()}")
class Store:
    def __init__(self,name):
        self.store_name=name
        self.mobile_list=[]
    def add_mobile(self,brand,model,price):
        mob = Mobile(brand,model,price)
        self.mobile_list.append(mob)
        print(f"Mobile '{brand} {model}' added successfully!\n")
    def display_all_mobiles(self):
        print(f"\nMobile Details of {self.store_name}")
        print("-" * 55)
        print("Brand\t\tModel\t\tPrice\t\tCategory")
        print("-" * 55)
        for mob in self.mobile_list:
            mob.display()
        print("-" * 55)
store = Store("XYZ Mobile Store")
while True:
    print("\n----- Mobile Store Management System -----")
    print("1. Add Mobile")
    print("2. Display All Mobiles")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        brand = input("Enter Brand: ")
        model = input("Enter Model: ")
        price = float(input("Enter Price: "))
        store.add_mobile(brand,model,price)
    elif choice==2:
        store.display_all_mobiles()
    elif choice==3:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")