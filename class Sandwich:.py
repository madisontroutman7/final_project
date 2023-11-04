class Sandwich:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.order_items = []

    def add_item(self, item):
        self.order_items.append(item)

    def calculate_total(self):
        total = sum(item.price for item in self.order_items)
        return total

class POSSystem:
    def __init__(self):
        self.menu = {

        }

    def display_menu(self):
        print("Menu:")
        for item in self.menu.values():
            print(f"{item.name} - ${item.price:.2f}")

    def take_order(self):
        order = Order()
        while True:
            self.display_menu()
            choice = input("Enter the name of the sandwich (or 'done' to finish): ")
            if choice == 'done':
                break
            if choice in self.menu:
                order.add_item(self.menu[choice])
            else:
                print("Invalid sandwich choice. Please select from the menu.")
        return order

    def process_order(self):
        order = self.take_order()
        if order.order_items:
            total = order.calculate_total()
            print("\nReceipt:")
            for item in order.order_items:
                print(f"{item.name} - ${item.price:.2f}")
            print(f"Total: ${total:.2f}")
        else:
            print("No items in the order.")

if __name__ == "__main__":
    pos = POSSystem()
    pos.process_order()