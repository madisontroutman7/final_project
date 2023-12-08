class Sandwich:
    """Represents a sandwich with a name and a price."""
    def __init__(self, name, price):
        """
        Initialize a Sandwich object

        Parameters:
        name(str): The name of the sandwich.
        price(float): The price of the sandwich.
        """
        self.name = name
        self.price = price

class Order:
    """Represents a customer's order"""
    def __init__(self):
        
        self.order_items = []

    def add_item(self, item):
        """
        Add a sandwich to the order
        Parameters:
        item (Sandwich): The sandwich to add to the order
        """
        self.order_items.append(item)

    def calculate_total(self):
        """
        Calculate the total price of the order
        Returns:
        float: The total price of the order
        """
        total = sum(item.price for item in self.order_items)
        return total

class POSSystem:
    """Represents a point of sale system for a sandwich shop."""
    def __init__(self):
        """Initialize a POSSystem object with a menu of sandwiches."""
        self.menu = {
        'BBQ Chicken': Sandwich('BBQ Chicken', 6.75),
        'Roast Beef': Sandwich('Roast Beef', 6.25),
        'Ruben': Sandwich('Ruben', 5.75),
        'Italian Cold Cut': Sandwich('Italian Cold Cut', 7.25),
        'Turkey': Sandwich('Turkey', 6.25),
        'Meatball Sub': Sandwich('Meatball Sub', 7.00),
        'Cheesesteak': Sandwich('Cheesesteak', 7.00)

        }

    def display_menu(self):
        """Display the menu with sandwich names and prices."""
        
        print("Menu:")
        
        for item in self.menu.values():
            print(f"{item.name} - ${item.price:.2f}")

    def take_order(self):
        """
        Take a customer's order by allowing them to select sandwiches from the menu.
        Returns:
        Order: The customer's order.
        """
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
        """Process a customer's order, calculate the total, and print a receipt."""
        
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