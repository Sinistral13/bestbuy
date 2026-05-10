class Product:
    def __init__(self, name, price, quantity):

        if not name:
            raise Exception("Invalid product name")
        if price < 0:
            raise Exception("Price cannot be negative")
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """Return quantity."""
        return self.quantity


    def set_quantity(self, quantity):
        """Set quantity. If quantity 0 or less, deactivate product."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self):
        """return active status"""
        return self.active


    def activate(self):
        """Activate self."""
        self.active = True


    def deactivate(self):
        """deactivate self"""
        self.active = False


    def show(self):
        """Print product variables."""
        print (f'Name: "{self.name}", '
               f'price: "{self.price}", quantity: "{self.quantity}"')


    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        """
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        total_price = self.price * quantity
        quantity += self.get_quantity()

        self.set_quantity(quantity)

        return total_price
    
def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
        main()
    