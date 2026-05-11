import products


class Store:
    """
    Represents a store that manages a list of products.

    The Store allows adding and removing products, tracking inventory,
    retrieving active products, and processing orders.
    """


    def __init__(self, product_list):
        """
        Initialize a Store with a list of products.

        Args:
            products (list): A list of Product objects available in the store.
        """
        self.product_list = product_list


    def get_products(self):
        """Return the product list"""
        return self.product_list


    def set_products(self, product_list):
        """Set product list"""
        self.product_list = product_list


    def add_product(self, product):
        """
        Add a product to the product list.
        Set the new list.
        """
        product_list = self.get_products()
        product_list.append(product)
        self.set_products(product_list)


    def remove_product(self, product):
        """
        Remove a product from the product list.
        Set the new list.
        """
        product_list = self.get_products()
        try:
            product_list.remove(product)
        except ValueError:
            print(f'Product "{product}" is not in list.')

        self.set_products(products)


    def get_total_quantity(self):
        """Return how many items are in the store in total."""
        product_list = self.get_products()
        quantity = 0
        for product in product_list:
            quantity += product.get_quantity()
        return quantity


    def get_all_products(self):
        """Return the list of all active products in the store."""
        product_list = self.get_products()
        active_products = []
        for product in product_list:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.get_products():
                print(f"Product {product.name} not in store.")
                continue
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

    best_buy = Store(product_list)
    availible_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    test = products.Product("Test", 400, 100)
    print(best_buy.order([(availible_products[0], 1), (availible_products[1], 2), (test, 6)]))


if __name__ == "__main__":
        main()
